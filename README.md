# Factroio Computer Compiler

Hello, this project contains a compiler made for a factorio general computer. Which makes it much easier to write understandable code for it. How to use it as well as the syntax of its programming language will be described in this README. And also any other behavior this compiler may have.

## How to use is

1. Start the exe
2. It will request that you choose a txt file to compile. Choose it
3. The the text file will be compiled and then converted into a blueprint string. The string will be automatically copied to your clipboard.
4. Import the blueprint in Factorio
5. Place the blueprint on top of the existing combinators
6. Turn the top left combinator off
7. Turn it on to begin execution

#### Language Structure
This compiler uses a custom, line-based programming language, which means:
Each line contains exactly one instruction.
A new line always starts a new instruction so no multi line statements.
At the lowest level, the compiler understands only three core instructions:
- `eval`
- `goto`
- `var`

However, by combining these basic instructions, the compiler can also interpret higher level structures like `if` statements and `while` loops.
Below, each instruction and its syntax will be explained.

## Syntax
### Var
Syntax: 
`var <name> <value>`
This declares a variable that can be referenced later in the program and assigns a starting value to it. There is no scope so these can be written anywhere. 
If no value is provided then it defaults to zero
### Eval
Syntax: 
Base form `eval <location> <var0> <operand> <var1>`
Or `<eval> <location> <expression>`
Calculates the expression and stores the result into the location variable.

The compiler accepts longer operations, even with parenthesis. For example
`eval <location> foo * bar + jab / (foo - bar)`. It will convert these into its base form automatically. 
### Goto
Syntax:  
Base form `goto <location> <var0> <operand> <var1>`
Or `<goto> <location> <expression>`
The goto instruction works just like the eval instruction. However, it performs a conditional jump based on the result of the expression. If the result is greater than 0 (i.e. the condition is true), the program will jump to the line number stored in `<location>`

There is no way to know what number each line has. So this is mostly used for the compiler to implement `while` and `if`. But there are some useful behaviors with it:
`goto 0 true` -> Restarts the program
`goto 400 true` -> Stops the program

The counter is an accesable variable as well. This mean you can store the counter at a specific part of the program and then jump there later, effectively making a label.
`eval label counter` -> Stores the jump location
`goto label true` -> Returns to the jump location

## Higher level syntax

### If
Syntax: 
```
if <expression>
    ...instructions...
endif
```
If the expression evaluates as true then it will execute all code after it. If it evaluates as false then it will skip everything until the endif. Works with nested ifs, consider using tab to make it easier to read.
### While
Syntax: 
```
while <expression>
    ...instructions...
endwhile
```
The while loop repeatedly executes the block of code between while and endwhile as long as the expression evaluates to true i.e. the result is greater than 0.

## Additional behavior

#### Predefined Variables
The compiler automatically provides several built in variables that your program can use:

**1. `in0` to `in4` Inputs**  
Represent the 5 input combinators on the left side.
Sending a signal to any of these will store its numeric value in the corresponding variable.

**2. `out0` to `out4` Outputs**  
Writing a value to one of these variables will output it through the matching output combinators on the right.

**3. `counter` Program Counter**  
Holds the line number of the instruction currently being executed.
Writing to `counter` causes the program to jump to that line, like a manual `goto`.

**4. `reg0` to `reg3` Temporary Registers**  
Used internally by the compiler to handle complex expressions.
Do not rely on them to store data their contents may be overwritten at any time.

**5. `greenLamp`, `yellowLamp`, `redLamp` Indicator Lamps**  
Writing a `TRUE` value, as in anything greater than 0 to one of these will turn the corresponding lamp on.
#### Immediate values
It is safe to use values directly in expressions. The compiler will automatically assign these an variable with that value. Only works if all characters are digits. Example:
```
var foo 3
eval foo 42 + bar
```
#### Direct assigning
Using an eval or goto but only using one variable will use that variable directly. For example:
In `eval foo bar` it will copy bar to foo. 
And in `goto label foo` it will go to label if foo is true.
#### Overflow
If a value is larger than 4194303 after execution then it will overflow and be stored as 0
#### No Floats nor negative numbers
All data in the system is stored and processed as unsigned integers only.
Floating point and negative number logic is not natively supported, but it can be implemented manually using custom logic. If you need such behavior, consider it an exercise left to the user.

## Examples
Ive included a few working tests and examples to show off how you can program the computer with this compiler in the folder `Compiler tests`. Here is an example of the Fibonacci algorithm, sending its values to output 0
```
var new 1
var old 0

# Check so it does not overflow
while old < (4190000 - new)
eval out0 new + old
eval old new
eval new out0
endwhile

eval greenLamp true & true
```
