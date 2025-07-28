import json
from turtle import position
import zlib
import base64
import pyperclip
import re
import copy
import msvcrt
from tkinter import Tk, filedialog
inputFile = "Everything Combinator.json"
outputJson = []
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


#   Functions

#Converts the json to a factorio string
def json_to_factorio_blueprint(json_data):
    json_string = json.dumps(json_data, separators=(',', ':'))
    compressed_data = zlib.compress(json_string.encode('utf-8'), level=9)
    base64_encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    blueprint_string = '0' + base64_encoded_data
    return blueprint_string    
def write_to_combinators(combinator, index, value, inputJson):
    entity = inputJson["blueprint"]["entities"][combinator]
    filters = (
        entity["control_behavior"]
        ["sections"]["sections"][0]
        ["filters"]
    )
    filters[index]["count"] = value
    return inputJson      
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
            print(f"Error: The file at {filePath} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No file selected or invalid file path.")
        quit()
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
# Conversion
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
                raise ValueError("Malformed postfix expression: not enough operands")
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


# Higher level functions


def whileCond(lines, i, inputJson, whileNum):
    expression = lines[i][1:]
    whileStart = i
    while i < len(lines) and lines[i][0] != "endwhile":
        i += 1
        if len(lines[i]) > 1 and lines[i][0] == "while":
            lines, i, inputJson, whileNum = whileCond(lines, i, inputJson, whileNum)
    if i < len(lines):
        lines[whileStart] = ["goto", f"whileStart{whileNum}"] + expression + ["~", "true"]
        lines[i] = ["goto", f"whileEnd{whileNum}", "true", "&", "true"]
    whileNum += 1
    return lines, i, inputJson, whileNum
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
    start.sort(key=lambda x: x[0])
    whileStart.sort(key=lambda x: x[0])
    whileEnd.sort(key=lambda x: x[0])

    for ending in whileEnd:
        _, inputJson = addVariable(f"whileEnd{ending[0]}", start[ending[0]][1] + 1, inputJson)
    for starting in whileStart:
        _, inputJson = addVariable(f"whileStart{starting[0]}", whileEnd[starting[0]][1] + 2, inputJson)
    for value in start:
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
#Creates location for jump regarding ifs
def ifFinder(lines, i, inputJson):
    name = lines[i][1]
    while i < len(lines) and lines[i] != ["eval", "endif", "true", "&", "true"]:
        i += 1
        if len(lines[i]) > 1 and lines[i][1].startswith("if"):
            lines, i, inputJson = ifFinder(lines, i, inputJson)
    _, inputJson = addVariable(name, i + 1, inputJson)
    print(i + 1)
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
        

#   Execution
#Resets the output, just in case                                  
with open("Everything Combinator.json", 'r') as src:
    outputJson = json.load(src)

#Loads the input      
lines = loadFile().splitlines()

#Tokenizes the lines
lines = tokenize(lines)     

#Higher level functions
lines, outputJson = whileFinder(lines, outputJson)
lines = ifCond(lines)

#Stores the value from "var foo 123" lines into a constant combinator, and keeps track of that mem position, removes the line afterwards
lines, outputJson = makeVariables(lines, outputJson)

#Breaks down equations with multiple operands into parts like: eval #mem0 #mem1 + #mem2
lines = parser(lines)
lines, outputJson = ifReplace(lines, outputJson)
whileReplace(lines, outputJson)


lineBackup = copy.deepcopy(lines)
#Replaces the tokens with machine code
for line in lines:
    line[0] = int(line[0] == "goto")
    for i in range(1, len(line)):
        token = line[i]        
        if token in operators:
            line[i] = operators[token]
        elif re.match(r'\w', token[0]):
            try:
                line[i] = variables.index(token)
            except ValueError:
                if i == 1 and line[0] == 0:
                    print("Error: Can not assign a new value to constant")
                    print(f"On line: {line}")
                    quit()
                if re.match(r'\d+', token):
                    line[i], outputJson = addVariable(token, int(token), outputJson)         

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
    