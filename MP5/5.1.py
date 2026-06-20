# Given list of numbers
numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39,
           71, 55, 41, 95, 70, 48, 42, 32, 13, 35]

# (a) Print the list
print("(a) List:")
print(numbers)

# (b) Print the average of the elements in the list
average = sum(numbers) / len(numbers)
print("\n(b) Average:")
print(average)

# (c) Print the largest and smallest values in the list
largest = max(numbers)
smallest = min(numbers)
print("\n(c) Largest and Smallest Values:")
print("Largest:", largest)
print("Smallest:", smallest)

# (d) Print the second largest and second smallest entries in the list
unique_numbers = sorted(set(numbers))

second_smallest = unique_numbers[1]
second_largest = unique_numbers[-2]

print("\n(d) Second Largest and Second Smallest Values:")
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)

# (e) Print how many even numbers are in the list
even_count = sum(1 for num in numbers if num % 2 == 0)
print("\n(e) Number of Even Numbers:")
print(even_count)

# (f) Print how many odd numbers are in the list
odd_count = sum(1 for num in numbers if num % 2 != 0)
print("\n(f) Number of Odd Numbers:")
print(odd_count)
