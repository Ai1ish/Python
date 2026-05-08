import random

number = random.randint(0, 36)

print("The spin resulted in", number)

if number == 0:
    print("Pay 0")

elif number % 2 == 0:
    print("Pay Black")
    print("Pay Even")

    if 1 <= number <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

else:
    print("Pay Red")
    print("Pay Odd")

    if 1 <= number <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
