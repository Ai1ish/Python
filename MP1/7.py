while True:
    try:
        value = float(input("Enter an integer: "))
        if value < 0:
            print("Please enter a non-negative integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
sum = (value * (value + 1)) / 2
print (f"The sum of the first {value} integers is {sum}.\n")