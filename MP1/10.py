import math
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log_a = math.log10(a)
exponentiation = a ** b

print (f"The sum of {a} and {b} is {sum}.")
print (f"The difference of {a} and {b} is {difference}.")
print (f"The product of {a} and {b} is {product}.")
print (f"The quotient of {a} and {b} is {quotient}.")
print (f"The remainder of {a} divided by {b} is {remainder}.")
print (f"log10 of {a} is {log_a}.")
print (f"{a} raised to the power of {b} is {exponentiation}.")