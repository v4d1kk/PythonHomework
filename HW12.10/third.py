x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))

max_number = x
if y > max_number:
    max_number = y
if z > max_number:
    max_number = z
print(max_number)
