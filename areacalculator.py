"""
Codecademy - Learn Python
Area Calculator
"""
print "Area Calculator"
# Prompt the user to select a shape
name = raw_input("Enter C for Circle or T for Triangle: ")
option = name

# Calculate the area of selected shape
  # Check if the user selected C for circle
if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = (radius ** 2) * 3.14159
  print "Area: %f" % area
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area: %f" % area
else:
  print "Invalid Input"

print "Program Exit"

# Print the area of the shape to user
