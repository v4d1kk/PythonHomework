import math

x = float(input())

if x < -20:
    y = x**2+5*x
elif x > 20:
    y = math.cos(3*x)+x/2
else:
    y = abs(3*x**3-10)
print(y)
