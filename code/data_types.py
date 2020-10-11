# Python Data Types

# Text Type: String

example = "Hello World. This is Python 101"
print("Variable type of example is", type(example))

# Numeric Types: Int
integer = 10
print("Variable type of integer is", type(integer))

# Numeric Types: floating

floating = 10.5
print("Variable type of floating is", type(floating))


# Numeric Types: complex
complex = 1j
print("Variable type of complex is", type(complex))


# Sequence Types: list

list_example = ["a", "b", "c", 1, 2, 3, False, True, 10.5, 10.6]
print("Variable type of list_example is", type(list_example))

# Sequence Types: tuple

tuple_example = ("a", "b", "c", 1, 2, 3, False, True, 10.5, 10.6)
print("Variable type of tuple_example is", type(tuple_example))

# Sequence Types: range
range_example = range(1, 11)
print("Variable type of range_example is", type(range_example))

# Mapping Type: dict
dict_example = {"first_name": "deepak", "last_name": "kaushik", "yoe": 5}
# print(dict_example.keys())
# print(dict_example.values())
print("Variable type of dict_example is {}".format(type(dict_example)))


# Boolean Type: bool

boolean_t = True
boolean_f = False
print("Variable type of boolean_t is {} and boolean_f is {}".format(type(boolean_t), type(boolean_f)))

