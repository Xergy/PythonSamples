import sys

Var1 = "x"
Var2 = "y"
Var3 = "z"

varList = [Var1,Var2,Var3]

ExpressStr = "Bob the uncle"

print(varList[0])

for expressVar in varList:
    code = f"""
print("Setting " + varList[0] + " to Bob")
{varList[0]} = \'{ExpressStr}\'
"""
    exec(code)
    print(x)



