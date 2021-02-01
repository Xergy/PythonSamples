import itertools
import sys

#msg = "Hello World"
#print(msg)
# /\ and , \/ or, > imples
x = False
y = False
z = True
#print(eval('a and (b or c)'))
#print(eval('not a and (b or c)'))

truths = list(itertools.product([True, False], repeat=3))

print(truths)
result = "~ x > y /\ ( y \/ z )"
#result = "x /\ ( y \/ z )"
result = "~ x > y /\ ( y \/ z )"
result = "x /\ y"
resultList = result.split()
print(resultList)
result = result.replace("/\\","and")
result = result.replace("\/","or")
result = result.replace("~","not")
result = result.replace("x > y","( not (x and not y))")
result = result.replace("x > z","( not (x and not z))")
result = result.replace("y > x","( not (y and not x))")
result = result.replace("y > z","( not (y and not z))")
result = result.replace("z > x","( not (z and not x))")
result = result.replace("z > y","( not (z and not y))")
print(result)
print("Results")
print(eval(result))

