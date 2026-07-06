# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Swapping the values
temp = a
a = b
b = c
c = temp

# Display the swapped values
print("After swapping:")
print("First number =", a)
print("Second number =", b)
print("Third number =", c)