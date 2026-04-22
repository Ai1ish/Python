import math
s = float(input("Enter the length of a side: "))

n = int(input("Enter the number of sides: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is {area}.")