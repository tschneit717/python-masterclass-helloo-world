age = 28
print("My age is " + str(age) + " years")
#                    Coerces an integer into a string
print("My age is {0} years".format(age))
# produces the same output
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# replacement fields are replaced with values in the parentheses after .format

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("I am {0}, my name is {0}, I am engaged to {1}, but my name is {0}"
      .format("Tom", "Anna"))

print(
    """Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}""".format("28", "30", "31"))
