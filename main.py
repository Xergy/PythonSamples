import inspect
import itertools
import sys

# Ask for number of input vars
#VarCount = input("Enter Number of vars: ")
VarCount = 3

# Build Input Table

inputs = list(itertools.product([True, False], repeat=VarCount))
print("Input Table")
print(inputs)

# Ask for input vars
#Var1 = input("Enter Var1: ")
#Var2 = input("Enter Var2: ")
#Var3 = input("Enter Var3: ")
Var1 = "x"
Var2 = "y"
Var3 = "z"

varList = [Var1,Var2,Var3]
print(varList)

# Ask for Sting to Evaluate, space delimited
#EvalStr = input("Enter String to eval: ")
#EvalStr = "X \/ ( y \/ z )".lower()
#EvalStr = "X \/ y \/ z".lower()
#EvalStr = "X /\ y /\ z".lower()
EvalStr = "( X /\ y ) /\ z".lower()


# Replace all easy string
## convert to lowers
print('Pre-Replacing Strings')
EvalSpit = EvalStr.split() 
print(EvalSpit)

print('Replacing String New Results')

SplitCounts = len(EvalSpit)
# print (SplitCounts)
# print (type(SplitCounts))

for Split in EvalSpit :
    print(Split)

print(EvalSpit)

for i, item in enumerate(EvalSpit):
    if item == "/\\" :
        EvalSpit[i] = "and"
    if item == "\/" :
        EvalSpit[i] = "or"
    if item == "~" :
        EvalSpit[i] = "not"

print(EvalSpit)

#TODO Detect Implies, and replace as needed

# Build ExpressStr

ExpressStr = ""

for Split in EvalSpit:
    print(Split)
    ExpressStr = ExpressStr + Split + " "

ExpressStr = ExpressStr.strip()

print(f"ExpressString = {ExpressStr}")

# Iterante Input Table create, new List

print(f"columnCount: {len(inputs[0]) + 1}")
columnCount = len(inputs[0]) + 1
print(f"RowCount: {len(inputs)}")
rowCount = len(inputs)

board = []    
for i in range(8): # create a list with nested lists
    board.append([])
    for n in range(4):
        board[i].append("O") # fills nested lists with data

print( (board[0])[0] )

for i, item in enumerate(inputs):
    print("New input loop")
    print(item)
    (board[i])[0] = item[0]  
    (board[i])[1] = item[1]  
    (board[i])[2] = item[2]

    for v, expressVar in enumerate(varList):
        print(expressVar)
        print(v)
        code = f"""
print("Setting {expressVar} to {item[v]}")
{expressVar} = \'{item[v]}\'
"""
        exec(code)

    result = eval(ExpressStr)
    print(f'ExpressStr = {ExpressStr}')
    print(result)
    (board[i])[3] = result


# Display List on screen

print("\nFinal Results:\n")

print(f"{Var1}\t{Var2}\t{Var3}\t{ExpressStr}")

for i in range(len(board)) :  
    for j in range(len(board[i])) :  
        print(board[i][j], end="\t") 
    print()    





