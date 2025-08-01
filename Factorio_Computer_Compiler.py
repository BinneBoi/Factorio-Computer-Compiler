import json
import zlib
import base64
import pyperclip
import re
import copy 
import msvcrt
from tkinter import Tk, filedialog
from data import everythingCombinator

inputFile = "Everything Combinator.json"
    
# Preset variables
variables = ["nan",
             "in0", "in1", "in2", "in3", "in4", 
             "out0", "out1", "out2", "out3", "out4", 
             "true", "false", "counter", 
             "redLamp", "yellowLamp", "greenLamp", 
             "reg0", "reg1", "reg2", "reg3"
             ]
# Valid operators
operators = {
   "+": 1,
   "-": 2,
   "*": 3,
   "/": 4,
   "%": 5,
   "^": 6,
   "<<": 7,
   ">>": 8,
   "&": 9,
   "|": 10,
   "~": 11,
   ">": 12,
   "<": 13,
   "==": 14,
   "!=": 15,
    }


# --- Functions ---
# Opens prompt to select which txt file to use
def loadFile():
    Tk().withdraw()
    filePath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])    
    if filePath and filePath.strip().lower() != "none":  
        try:
            with open(filePath, "r") as file: 
                print("File contents successfully read.")
                return file.read()            
        except FileNotFoundError:
            print("Could not find 'Everything Combinator.json' make sure it is included in the same directory as the executable")
            input("Press enter to quit...")
            quit()
    else:
        print("No file selected or invalid file path.")
        input("Press enter to quit...")
        quit()
# Tokenizes the lines using regex
def tokenize(lines):
    output = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            continue
        if line.startswith("var"):
            tokens = line.split()
            output.append(tokens)
        else:
            escaped_ops = [re.escape(op) for op in operators.keys()]
            pattern = (
                r"("
                + r"|".join(escaped_ops)
                + r"|\w+"
                + r"|\(|\)"
                + r")"
                )
            tokens = re.findall(pattern, line)
            output.append(tokens)          
    return output   
# Takes the combinator json and writes the specified value at index position
def write_to_combinators(combinator, index, value, inputJson):
    entity = inputJson["blueprint"]["entities"][combinator]
    filters = (
        entity["control_behavior"]
        ["sections"]["sections"][0]
        ["filters"]
    )
    filters[index]["count"] = value
    return inputJson      
# Converts the json to a factorio string
def json_to_factorio_blueprint(json_data):
    json_string = json.dumps(json_data, separators=(',', ':'))
    compressed_data = zlib.compress(json_string.encode('utf-8'), level=9)
    base64_encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    blueprint_string = '0' + base64_encoded_data
    return blueprint_string 

# Checks for any assigning evals, as in evals that copies values from one cell to another. As in eval foo bar
# Then adds an "* true* at the end of it to make it viable for the rest of the compiler
def assigning(lines):
    for line in lines:
        if (line[0] == "eval" or line[0] == "goto") and len(line) == 3:
            line.append("*")
            line.append("true")
        if line[0] == "while" and len(line) == 3:
            line.append("*")
            line.append("true")
    return lines            
# Checks for syntax errors
def errorCheck(lines):
    errors = 0
    whilestart = 0
    whileend = 0
    ifstart = 0
    ifend = 0
    # First pass: Count control structures
    for line in lines:
        for token in line:
            if token == "while":
                whilestart += 1
            if token == "endwhile":
                whileend += 1
            if token == "if":
                ifstart += 1
            if token == "endif":
                ifend += 1
    # Check for mismatched blocks
    if whilestart != whileend:
        print(f"Error: Number of 'while' and 'endwhile' blocks do not match ({whilestart} vs {whileend})")
        errors += 1
    if ifstart != ifend:
        print(f"Error: Number of 'if' and 'endif' blocks do not match ({ifstart} vs {ifend})")
        errors += 1
    # Second pass, per line checks
    for index, line in enumerate(lines):
        if not line:
            continue
        command = line[0]
        arg_count = len(line) - 1
        # Check so there are no overflow values
        for token in line:
            if token.isdigit():
                value = int(token)
                if value > 4194303:
                    print(f"Error on line {index}: Value must be lower than 4194303, got {value}")
                    errors += 1
                if value < 0:
                    print(f"Error on line {index}: Value must be positive, got {value}")
                    errors += 1                     
        # eval
        if command == "eval":
            if len(line) < 3:
                print(f"Error on line {index}: 'eval' requires at least 2 arguments, got {arg_count}")
                errors += 1
        # goto
        elif command == "goto":
            if len(line) < 3:
                print(f"Error on line {index}: 'goto' requires at least 2 arguments, got {arg_count}")
                errors += 1
        # var
        elif command == "var":
            if len(line) < 2 or len(line) > 3:
                print(f"Error on line {index}: 'var' requires exactly 2 arguments, got {arg_count}")
                errors += 1
            else:
                varname = line[1]
                if varname.startswith("while"):
                    print(f"Error on line {index}: Variable name cannot start with 'while'")
                    errors += 1
                if varname.startswith("if"):
                    print(f"Error on line {index}: Variable name cannot start with 'if'")
                    errors += 1
                if varname.isdigit():
                    print(f"Error on line {index}: Variable name cannot be digits only")
                    errors += 1
        # delay
        elif command == "delay":
            if len(line) != 2:
                print(f"Error on line {index}: 'delay' requires exactly 1 argument, got {arg_count}")
                errors += 1
            else:
                try:
                    delay_val = int(line[1])
                    if delay_val > 2000000:
                        print(f"Error on line {index}: Delay cannot be more than 2 million")
                        errors += 1
                    if delay_val < 1:
                        print(f"Error on line {index}: Delay must be at least 1")
                        errors += 1
                except ValueError:
                    print(f"Error on line {index}: Delay argument must be a valid integer")
                    errors += 1
        # if
        elif command == "if":
            if len(line) < 2:
                print(f"Error on line {index}: 'if' requires at least 1 argument, got {arg_count}")
                errors += 1
        # while
        elif command == "while":
            if len(line) < 2:
                print(f"Error on line {index}: 'while' requires at least 1 argument, got {arg_count}")
                errors += 1
                
    if errors > 0:
        print(f"\nCompilation failed with {errors} error(s).")
        input("Press enter to quit...")
        quit()

    return lines


# Shunting yard algorithm using recursion for the postfix conversion
def infixToPostfix(tokens):
    stack = []
    postfixList = []
    #Priority for each operator
    priority_map = {
   "|": 0,
   "~": 1,
   "&": 2,
   "==": 3,
   "!=": 3,
   "<": 4,
   ">": 4,
   "<<": 5,
   ">>": 5,
   "+": 6,
   "-": 6,
   "*": 7,
   "/": 7,
   "%": 7,
   "^": 8
    }
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if re.match(r'^\w', token[0]):  
            postfixList.append(token)
        elif token in priority_map: 
            while (
                len(stack) > 0 and
                stack[-1] in priority_map and
                priority_map[token] <= priority_map[stack[-1]]
            ):
                postfixList.append(stack.pop())
            stack.append(token)
        elif token == "(":
            index = i + 1
            depth = 1
            while index < len(tokens) and depth > 0:
                if tokens[index] == "(":
                    depth += 1
                elif tokens[index] == ")":
                    depth -= 1
                index += 1
            if depth != 0:
                raise ValueError("Unmatched parentheses")
            postfixList.extend(infixToPostfix(tokens[i + 1: index - 1]))
            i = index - 1
        else:
            print("Invalid token:", token)
        i += 1  
    stack.reverse()
    postfixList.extend(stack)
    return postfixList
# Turns input values into the form: eval dest mem1 op mem2
def evalCreater(dest, mem1, mem2, op):
    output = ["eval", dest]
    output.append(mem1)
    output.append(op)
    output.append(mem2)
    return output
# Converts each expression to postfix, then breaks it into sequential register based operations in correct order
# Example: eval location foo + bar * jab -> eval reg0 bar * jab, eval location foo + reg0
def parser(lines):
    new_lines = []
    ifNum = 0
    for expression in lines:
        
        operation = expression[0]
        location = expression[1]
        equation = expression[2:]
        
        postfix = infixToPostfix(equation)
        output = []
        reg_counter = 0
        while len(postfix) > 0:
            i = 0
            while i < len(postfix) and postfix[i] not in operators:
                i += 1
            if i == len(postfix):
                break
            if i < 2:
                print(f"Error: Malformed postfix expression")
                print(f"On line: {expression}")
                input("Press enter to quit...")
                quit()
            arg1 = postfix[i - 2]
            op = postfix[i]
            arg2 = postfix[i - 1]
            if isinstance(arg2, str) and arg2.startswith("reg"):
                dest = arg2
            elif isinstance(arg1, str) and arg1.startswith("reg"):
                dest = arg1
            else:
                dest = f"reg{reg_counter}"
                reg_counter += 1
            output.append(evalCreater(dest, arg1, arg2, op))
            if len(postfix) == 3:
                postfix.pop(i) 
                output[-1][1] = location
                output[-1][0] = operation
            else:
                postfix[i] = dest
            postfix.pop(i - 1)
            postfix.pop(i - 2)
        #For handling while loops, start{value} is a temporary marker    
        if expression[1].startswith("whileStart"):
           match = re.search(r"\d+", expression[1])
           value = match.group()
           output[0].append(f"start{value}")
        new_lines.extend(output)
    return new_lines

# Writes predefined memory into the RAM combinator
def addVariable(name, value, inputJson):
    variables.append(name)
    pos = len(variables)
    value = value | (pos << 22)
    inputJson = write_to_combinators(0, pos - 1, value, inputJson)    
    return pos - 1, inputJson
# Writes all variables defined with var verb into the RAM combinator
def makeVariables(lines, inputJson):
    outputLines = []
    for line in lines:
       if line[0] == "var":
           value = int(line[2] if len(line) > 2 else 0)
           _, inputJson = addVariable(line[1], value, inputJson)
       else:
           outputLines.append(line)            
    # Set true variable to 1
    inputJson = write_to_combinators(0, variables.index("true"), 1 | (((int(variables.index("true")) + 1) << 22)), inputJson)
    # Set clock to 1 to make program execution start on load
    inputJson = write_to_combinators(0, variables.index("counter"), 58720257, inputJson)
    return outputLines, inputJson


# --- Higher level functions ---
# Converts 'while' and 'endwhile' statements into low-level 'goto' instructions.
def whileCond(lines, i, inputJson, whileNum):
    expression = lines[i][1:]
    whileStart = i
    while i < len(lines) and lines[i][0] != "endwhile":
        i += 1
        if len(lines[i]) > 1 and lines[i][0] == "while":
            # Recursively process nested 'while' statements
            lines, i, inputJson, whileNum = whileCond(lines, i, inputJson, whileNum)
    if i < len(lines):
        lines[whileStart] = ["goto", f"whileStart{whileNum}"] + expression + ["~", "true"]
        lines[i] = ["goto", f"whileEnd{whileNum}", "true", "&", "true"]
    whileNum += 1
    return lines, i, inputJson, whileNum
# Scans the code for 'while' statements and replaces them with 'goto' statements.
# Also assigns a unique label to each loop for proper jump location tracking.
def whileFinder(lines, inputJson):
    i = 0
    whileNum = 0
    while i < len(lines): 
        if lines[i][0] == "while":
            lines, i, inputJson, whileNum = whileCond(lines, i, inputJson, whileNum)
        i += 1
    return lines, inputJson
def whileReplace(lines, inputJson):
    i = 0
    start = []
    whileStart = []
    whileEnd = []
    # Identify and collect indices of loop labels and their corresponding positions
    while i < len(lines):
        value = []
        if lines[i][-1].startswith("start"):
            match = re.search(r"\d+", lines[i][-1])
            value = match.group()
            start.append([int(value), i])
        if lines[i][1].startswith("whileStart"):
            match = re.search(r"\d+", lines[i][1])
            value = match.group()
            whileStart.append([int(value), i])
        if lines[i][1].startswith("whileEnd"):
            match = re.search(r"\d+", lines[i][1])
            value = match.group()
            whileEnd.append([int(value), i])   
        i += 1
    # Ensure all label lists are sorted by loop number for proper indexing
    start.sort(key=lambda x: x[0])
    whileStart.sort(key=lambda x: x[0])
    whileEnd.sort(key=lambda x: x[0])

    for ending in whileEnd:
        _, inputJson = addVariable(f"whileEnd{ending[0]}", start[ending[0]][1] + 1, inputJson)
    for starting in whileStart:
        _, inputJson = addVariable(f"whileStart{starting[0]}", whileEnd[starting[0]][1] + 2, inputJson)
    for value in start:
        # Clean up the original 'start' marker from the line
        lines[value[1]].pop()
        
    return lines, inputJson
    
# Transforms 'if' and 'endif' statements into low-level control flow instructions
# so they can be correctly interpreted by the rest of the compiler
def ifCond(lines):
    ifNum = 0
    for i in range(len(lines)):
        if lines[i][0] == "if":
            lines[i] = ["goto", f"if{ifNum}", "("] + lines[i][1:] + [")", "~", "true"]
            ifNum += 1
        elif lines[i][0] == "endif":
            lines[i] = ["eval", "endif", "true", "&", "true"]
    return lines
# Goes through the code and replaces ifs with goto and adds a jump location variable for it
def ifFinder(lines, i, inputJson):
    name = lines[i][1]
    while i < len(lines) and lines[i] != ["eval", "endif", "true", "&", "true"]:
        i += 1
        if len(lines[i]) > 1 and lines[i][1].startswith("if"):
            lines, i, inputJson = ifFinder(lines, i, inputJson)
    _, inputJson = addVariable(name, i + 1, inputJson)
    if i < len(lines):
        del lines[i]

    return lines, i, inputJson
def ifReplace(lines, inputJson):
    i = 0
    while i < len(lines): 
        if len(lines[i]) > 1 and lines[i][1].startswith("if"):
            lines, i, inputJson = ifFinder(lines, i, inputJson)
        i += 1
    return lines, inputJson
        
# Implements the delay function
def estimate_iterations(t):
    return t / (0.6 + 0.433 / t)
def delay(lines):
    delayNum = 0
    i = 0
    while i < len(lines):
        if lines[i][0] == "delay":
            output = []
            delayTime = int(lines[i][1])
            del lines[i]
            delayVar1 = f"delay{delayNum}"
            delayVar2 = f"{delayVar1}x"
            output.append(["var", delayVar1, f"{round(estimate_iterations(delayTime))}"])
            output.append(["var", delayVar2, "0"])
            output.append(["eval", delayVar2, "false", "*", "false"])
            output.append(["while", delayVar1, ">", delayVar2]) 
            output.append(["eval", delayVar2, delayVar2, "+", "1"]) 
            output.append(["endwhile"]) 
            for j, instruction in enumerate(output):
                lines.insert(i + j, instruction)
            delayNum += 1
        i += 1
    return lines
            

# --- Execution ---
# Loads the json containing the three combinators all instructions will be written to                                  
outputJson = json.loads(everythingCombinator)

# Loads the input
print("Please select txt to compile...")       
lines = loadFile().splitlines()
# Tokenizes the lines
lines = tokenize(lines) 
# Handles direct assignings
lines = assigning(lines)
lines = errorCheck(lines)

# Adds user specified delays
lines = delay(lines)
# Stores the value from "var foo 123" lines into a constant combinator, and keeps track of that mem position, removes the line afterwards
lines, outputJson = makeVariables(lines, outputJson)

# Higher level functions
lines, outputJson = whileFinder(lines, outputJson)
lines = ifCond(lines)

# Breaks down equations with multiple operands into parts like: eval #mem0 #mem1 + #mem2
lines = parser(lines)
# Apply higher-level transformations after parsing, since line positions may have changed.
lines, outputJson = ifReplace(lines, outputJson)
whileReplace(lines, outputJson)
# Copy for feedback
lineBackup = copy.deepcopy(lines)

# Replaces the tokens with machine code
for line in lines:
    # Goto == 1, eval == 0
    line[0] = int(line[0] == "goto")
    for i in range(1, len(line)):
        token = line[i]        
        if token in operators:
            line[i] = operators[token]
        elif re.match(r'\w', token[0]):
            # Check if the token exists
            # If it doesn't and it's a numeric constant, automatically create a new variable with that value
            try:
                line[i] = variables.index(token)
            except ValueError:
                if token.isdigit():
                    line[i], outputJson = addVariable(token, int(token), outputJson)
                else:
                    print(f"Unkown variable: {token}")
                    input("Press enter to quit...")
                    quit()

loop = 1
for line in lines:
    jump    =   int(line[0])
    pos     =   int(line[1])
    load1   =   int(line[2]) 
    operand =   int(line[3])
    load2   =   int(line[4])    
    load = (loop + 1) << 22
    load |= (load1 << 13)
    load |= (load2 << 4)
    load |= operand  
    store = (loop + 1) << 22
    store |= pos << 1
    store |= jump    
    outputJson = write_to_combinators(1, loop, load, outputJson)
    outputJson = write_to_combinators(2, loop, store, outputJson)
    loop += 1

#Output
output = json_to_factorio_blueprint(outputJson)
print("Final pass before becoming machine code:")
for line in lineBackup: print(line)
print(f"\nVariables and constants used: {variables[21:]}")
print(f"RAM used: {len(variables)}/400")
print(f"ROM used: {len(lines)}/400")
try:
    pyperclip.copy(output)
    print("\nFactorio blueprint string has been copied to clipboard.")
except ValueError:
    print(output)
print("If blueprint was not copied to clipboard, press b to print it in the terminal. Press anything else to end")
if msvcrt.getch() in (b'b', b'B'):
    print(output)
else:
    quit()
    