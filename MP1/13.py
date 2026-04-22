
cents = int(input("Enter the number of cents: "))

toonies = cents // 200
cents = cents % 200

loonies = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

print("Change to give:")
print(f"Toonies: {toonies}")
print(f"Loonies: {loonies}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")