import math
# Take two numbers as user input and print addition, subtraction and multiplication of it
a = int(input("Please enter 1st number: "))
b = int(input("Please enter 2nd number: "))
print("Add:", a + b)
print("Subtract :", a - b)
print("Product: ", a * b)
print("Division: ", a / b)
print("Modulus= ", a % b)
# Print a^2 + b^2 + 2ab
print("a + b whole square: " , a * a + 2 * a * b + b * b)
# a^2 is equal to a**2
print(a**2)
# floor division equals to //
print(10//3)
# math is a default package and floor and ceil are 2 functions of it.
# In order to call them, we need to use dot notation that is package_name.function_name
# Since math is not a built in function, we need to import it before calling just like in line no 1, that is import package_name.
print(math.floor(5.5))
print(math.ceil(5.5))
