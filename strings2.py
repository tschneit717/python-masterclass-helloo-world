#                   1
#         01234567890123
parrot = "Norwegian Blue"
print(parrot)

string = "We win"

for i in range(len(string)):
    print(string[i])

backwardsString = "retaw"
#              start (default 0), stop, step (default 1)
for i in range(len(backwardsString), 0, -1):
    print(backwardsString[i - 1])

# slice mechanics, [start:stop:step]
# Up to but NOT including stop index
print(parrot[0:6])  # splits from 0 to index 6, but not including 6
print(parrot[:2])   # splits from default 0 to index 2
print(parrot[10:])  # splits starting from 10 to the end of string
print(parrot[10::2])  # splits starting from 10 to the end of string, printing every second character
print(parrot[::2])  # prints every second character for the whole string
print(parrot[::-2])  # prints every second character for the whole string, but in reverse order
print(parrot[-4::1])  # starting at the 4th from the end index, stepping 1 each time

