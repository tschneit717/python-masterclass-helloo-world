string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")
print("Hello " * 5)
# print("Hello " * 5 + 4)  # throws an error because of the order of operations
print("Hello " * (5 + 4))  # Evaluates correctly
print("Hello " * 5 + "4")  # Evaluates correctly, but adds 4 to the end

today = "friday"
print("day" in today)  # should evaluate to True
print("fri" in today)  # should evaluate to True
print("thur" in today)  # should evaluate to False
print("Parrot" in "Fjord")  # should evaluate to False
