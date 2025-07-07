import json
from turtle import position
import zlib
import base64
import pyperclip
import re
from tkinter import Tk, filedialog
filename = "Everything Combinator.json"
variables = ["nan","in0", "in1", "in2", "in3", "in4", "out0", "out1", "out2", "out3", "out4", "true", "false", "counter", "redLamp", "yellowLamp", "greenLamp", "reg"]

# Converts the json to a factorio string
def json_to_factorio_blueprint(json_data):
    json_string = json.dumps(json_data, separators=(',', ':'))
    compressed_data = zlib.compress(json_string.encode('utf-8'), level=9)
    base64_encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    blueprint_string = '0' + base64_encoded_data
    return blueprint_string    

def write_to_combinators(combinator, index, value, filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    entity = data["blueprint"]["entities"][combinator]
    filters = (
        entity["control_behavior"]
        ["sections"]["sections"][0]
        ["filters"]
    )
    filters[index]["count"] = value
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
       
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

arg_map = {
   "eval": 0,
   "goto": 1,
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
   "xor": 11,
   ">": 12,
   "<": 13,
   "==": 14,
   "!=": 15,
    }

def tokenize(file):
    lines = file.split("\n") 
    new_lines = []
    for line in lines:
        args = line.split()
        for i, arg in enumerate(args):
            if arg == "<":
                args[i] = str(13)
            elif arg == ">":
                args[i] = str(12)
            else:
                args[i] = str(arg_map.get(arg.strip(), arg.strip()))

        new_lines.append(args)
    
    return new_lines 
        
def makeVariables(new_lines, file):
    filtered_lines = []
    for line in new_lines:
       if line[0] == "var":
           varname = line[1]
           variables.append(varname)
           value = int(line[2] if len(line) > 2 else 0)
           value = value | (((int(variables.index(varname)) + 1) << 22))
           write_to_combinators(0, variables.index(varname), value, file)
       else:
           filtered_lines.append(line)
                
    # Set true variable to 1
    write_to_combinators(0, variables.index("true"), 1 | (((int(variables.index("true")) + 1) << 22)), file)
    # Set clock to 1 to make program execution start on load
    write_to_combinators(0, variables.index("counter"), 58720257, file)
    return filtered_lines

'''
# Resets the output                                  
with open("Everything Combinator.json", 'r') as src:
    data = json.load(src)
with open("Output.json", 'w') as dest:
    json.dump(data, dest, indent=4) 

# 

file = loadFile()
tokens = tokenize(file)
tokens = makeVariables(tokens, "Output.json")

loop = 1
for line in tokens:
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
    
    write_to_combinators(1, loop, load, "Output.json")
    write_to_combinators(2, loop, store, "Output.json")
    loop += 1
with open("Output.json", 'r') as src:
    data = json.load(src)
    output = json_to_factorio_blueprint(data)
    
    
print(output)
'''

# Shunting yard algorithm, with recursion for fun
def infixToPostfix(tokens):
    stack = []
    postfixList = []
    priority_map = {
   "|": 0,
   "xor": 1,
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
        if token[0] == "#":  
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
def evalCreater(mem1, mem2, op):
    output = ["eval", "#reg"]
    output.append(mem1)
    output.append(op)
    output.append(mem2)
    return output
def tokenize_expression(line):
    line = line.strip()
    if line.startswith("var"):
        tokens = line.split()
        return tokens
    escaped_ops = [re.escape(op) for op in arg_map.keys()]
    pattern = (
        r"("
        + r"|".join(escaped_ops)
        + r"|\#\w+"
        + r"|\(|\)"
        + r")"
    )
    tokens = re.findall(pattern, line.replace(" ", ""))
    return tokens
def parser1(expression):
      operation = expression[0]
      location = expression[1]
      equation = expression[2:]
      postfix = infixToPostfix(equation)
      output = []
      while len(postfix) > 0:
        i = 0
        while postfix[i] not in arg_map:
            i += 1
        arg1 = postfix[i - 2]
        op = postfix[i]
        arg2 = postfix[i - 1]
        output.append(evalCreater(arg1, arg2, op))
        print(evalCreater(arg1, arg2, op))
        if len(postfix) == 3:
            postfix.pop(i)
            output[-1][1] = location
            output[-1][0] = operation
        else:
            postfix[i] = "reg"    
        postfix.pop(i-1)
        postfix.pop(i-2)
      return output
        


#Resets the output, just in case                                  
with open("Everything Combinator.json", 'r') as src:
    data = json.load(src)
with open("Output.json", 'w') as dest:
    json.dump(data, dest, indent=4) 
#Loads the input      
file = loadFile()
lines = file.splitlines()
#Tokenizes the lines
tokenized_lines = []
for line in lines:
  tokenized_lines.append(tokenize_expression(line))
#Stores the value from "var foo 123" lines into a constant combinator, and keeps track of that mem position, removes the line afterwards
lines = makeVariables(tokenized_lines, "Output.json")    
#Breaks down equations with multiple operands into parts like: eval #mem0 #mem1 + #mem2
new_lines = []
for line in lines:
    new_lines.extend(parser1(line))    
#Inserts the mem positions
for line in new_lines:
    for i in range(len(line)):
        arg = line[i]
        if arg[0] == '#':
            line[i] = variables.index(arg[1:])
        elif arg in arg_map:
            line[i] = arg_map[arg]

loop = 1
for line in new_lines:
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
    
    write_to_combinators(1, loop, load, "Output.json")
    write_to_combinators(2, loop, store, "Output.json")
    loop += 1
with open("Output.json", 'r') as src:
    data = json.load(src)
    output = json_to_factorio_blueprint(data)
    
    
print(output)