
numbers = [18, 19, 20]

print("GROUP 5:")
print("Name: CALANOC, ASH")
print("Name: NARVASA, AILISH SOPHIA D.")
print("Name: RODIL, JAYSON CLEM")
print("Name: SUMLIHIG, GWYNETH")
print("School: FEU TECH")
print("Machine Problem - 2")

print("Original list", numbers)

# (a) Set the second entry (index 1) to 17
numbers[1] = 17
print("a", numbers)

# (b) Add 4, 5, and 6 to the end of the list
numbers.extend([4, 5, 6])
print("b", numbers)

# (c) Remove the first entry from the list
numbers.pop(0)
print("c", numbers)

# (d) Sort the list
numbers.sort()
print("d", numbers)

# (e) Double the list
numbers = numbers * 2
print("e", numbers)

# (f) Insert 25 at index 3
numbers.insert(3, 25)
print("f", numbers)
