print("Hello, world!")


def function(x, y):
    return x * y


print(function(2, 10))

for x in range(120):
    if x % 12 == 0:
        print(x)

name = input('Name: ')
print("Hello man", 21, f"Whats up {name}", function(12, 12))
