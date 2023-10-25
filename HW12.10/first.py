import math

x = float(input())

if -10 < x < 10:
    y = math.sqrt(3 * x - 5)
else:
    y = 1 - math.tan(abs(x - 15))
print(y)
