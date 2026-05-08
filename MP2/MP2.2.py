year = int(input("Enter a year: "))

animals = [
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Hare"
]

index = year % 12

print("The animal is", animals[index])
