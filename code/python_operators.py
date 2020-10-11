#  https://www.javatpoint.com/python-operators
#  https://www.w3schools.com/python/python_operators.asp

##############################
# Arithmetic Operators: +, -, *, /, %, //, **
##############################

print(4 + 2)  # 6
print(4 - 2)  # 2
print(4 * 2)  # 8
print(4 / 2)  # 2.0
print(4 % 2)  # 0
print(4 // 3)  # 1
print(4 ** 2)  # 16

##############################
# **Comparison operator
##############################

# ==  : (If the value of two operands is equal, then the condition becomes true)

print(2 == 2)  # True
print(2 == 3)  # False

# != : (If the value of two operands is not equal, then the condition becomes true.)

print(2 != 2)  # False
print(2 != 3)  # True

# <= (If the first operand is less than or equal to the second operand, then the condition becomes true.)
# >= (If the first operand is greater than or equal to the second operand, then the condition becomes true.)
# > (If the first operand is greater than the second operand, then the condition becomes true.)
# < (If the first operand is less than the second operand, then the condition becomes true.)


##############################
# *Assignment Operators
##############################

# = (It assigns the value of the right expression to the left operand.)

var_one = 1
print(var_one)

# += (It increases the value of the left operand by the value of the right operand and assigns
# the modified value back to left operand.
# For example, if a = 10, b = 20 => a+ = b will be equal to a = a+ b and therefore, a = 30.)

var_two = 2
var_two += 5   # var_two = var_two + 5
print(var_two)

# -= (It decreases the value of the left operand by the value of the right operand and assigns
# the modified value back to left operand.
# For example, if a = 20, b = 10 => a- = b will be equal to a = a- b and therefore, a = 10.)

# *= (It multiplies the value of the left operand by the value of the right operand and assigns
# the modified value back to then the left operand.
# For example, if a = 10, b = 20 => a* = b will be equal to a = a* b and therefore, a = 200.)

# %= (It divides the value of the left operand by the value of the right operand and assigns the reminder back to the
# left operand. For example, if a = 20, b = 10 => a % = b will be equal to a = a % b and therefore, a = 0.)

# **=  (a**=b will be equal to a=a**b, for example, if a = 4, b =2, a**=b will assign 4**2 = 16 to a.)

# //=  (A//=b will be equal to a = a// b, for example, if a = 4, b = 3, a//=b will assign 4//3 = 1 to a.)


##############################
# Bitwise Operators (Read and explain)
# & : binary and
# | : binary or
# ^ : binary xor
# ~ : negation
# << : left shift
# >> : right shift
##############################


##############################
# *Logical Operators
##############################
a = 2
b = 1
# and

###
#  1 1 == 1
# else 0
###

if a == 2 and b == 1:
    print("AND: True")

if a == 2 and b == 2:
    print("AND: True")

# or

# 0 0 == 0
# else 1

if a == 2 or b == 1:
    print("OR: True")

if a == 2 or b == 2:
    print("OR: True")

if a == 3 or b == 3:
    print("OR:  True")

# not

if a == 2 and not b == 4:
    print("NOT Ops")


###############################
# *Membership Operators
##############################

# in
# not in

list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 10

if a in list_example:
    print("Found")

if a not in list_example:
    print("NOT found")

###############################
# *Identity Operators
###############################

# is
# not is

a = True
b = False

if a is True:
    print("True")

if b is not True:
    print("False")