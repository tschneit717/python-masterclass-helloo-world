#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"
# omitting the stop value iterates through the whole string, while a 0 omits the starting character, and -1 stops at
# the second last char
backwards = letters[len(letters) - 1::-1]
# This is the same as the line above
backwards2 = letters[::-1]
print(backwards)
print(backwards2)

chal1 = letters[16:13:-1]
chal2 = letters[4::-1]
chal3 = letters[:-9:-1]

print(chal1)
print(chal2)
print(chal3)

# String
# list
# tuple
# range
# bytes and byte array

# a sequence is defined as an ordered set of items
# ex: "Hello World", or ["Computer", "Python", "Program"]
# Because a sequence is ordered, we can use indexes to access individual items
# we can index within a sequence of indexes: list[0][4]

# ranges are a sequence that cannot be concatenated