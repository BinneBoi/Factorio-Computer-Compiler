import json
from turtle import position
import zlib
import base64
import pyperclip
from tkinter import Tk, filedialog
filename = "Everything Combinator.json"
arg_map = {
   "eval": 0,
   "goto": 1,
   "+": 1,
   "-": 2,
   "*": 3,
   "/": 4,
   "%": 5,
   "^": 6,
   "<": 7,
   ">": 8,
   "xor": 9
    }
variables = ["nan","in0", "in1", "in2", "in3", "in4", "out0", "out1", "out2", "out3", "out4", "true", "false"]

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
   "&&": 9,
   "|": 10,
   "xor": 11,
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
    for line in filtered_lines:
        for i in range(len(line)):
            arg = line[i]
            if arg[0] == '#':
                line[i] = variables.index(arg[1:])
                
    # Set true variable to 1
    write_to_combinators(0, variables.index("true"), 1 | (((int(variables.index("true")) + 1) << 22)), file)
    return filtered_lines

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