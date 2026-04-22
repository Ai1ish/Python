
length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))

area_sqft = length * width
area_acres = area_sqft / 43560

print (f"The are of the field is {area_sqft:.2f} square feet.")