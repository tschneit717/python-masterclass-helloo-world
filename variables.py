# python variable rules:
# python names must begin with a letter or an underscore
# they can contain letters, nums, or underscores but cannot bein with nums
# vars are case-sensitive
# vars are created when an = is used to assign

age = 28
print(age)
name = "Tom"
sentence = name + "is " + str(age) + " years old"
age = "28 years old"
print(type(sentence))
print(type(name))
print(type(age))

# Binding a variable to a value, as opposed to binding a value to a variable
# Python IS strongly typed
# ex: name + "is " + age + " years old"
# This will fail due to typeerror

# Types in python
# Strings "String"
# Int 1
# Float 1.0
# complex numbers, include real and imaginary parts of numbers)
# Boolean True/False
# Set { "x": 1, "why": 12 }
# List ["One", "Two"]
# Dict { x: 1 }
# Tuple (1, 2, 3)
