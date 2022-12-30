for i in range(1, 13):
    # {0:2} the second value is the width, reserving spaces for those values
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


for i in range(1, 13):
    # You can include a < to left align your formatting, ex: {1:<3}
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

for i in range(1, 13):
    # You can include a ^ to center align your formatting, ex: {1:<3}
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()
# When specifying a floating point value, it defaults to 6. However, we can specify precision
# f to make a format a floating point, .50f to change precision
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:<12.50f}".format(22 / 7))
print("Pi is approximately {0:<52.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))

# Field numbers are not required in formatting
# ex:
for i in range(1, 13):
    # You can include a ^ to center align your formatting, ex: {1:<3}
    print("No. {:2} squared is {:^3} and cubed is {:^4}".format(i, i ** 2, i ** 3))

# if you do not include field numbers, cannot use val more than once or change the order
# in which they're used


# fstrings are not ported back to py3 earlier than 3.6
age = 28
print(f"My age is {str(age)}")
print(f"Pi is approximately {22 / 7:12.50f}")

# python 2 string interpolation, is deprecated
print("My age is %d years" % age)
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 5, minor))
print("PI is approximately %f" % (22 / 7))
print("PI is approximately %60.50f" % (22 / 7))
