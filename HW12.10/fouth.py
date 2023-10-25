import math

x = int(input())
if x < -5:
    y = x**2
    z = math.tan(abs(x+3))
    print(z)
elif x > 10:
    y = abs(math.cos(3*x)+x/2)
else:
    y = x+5
print(y)
