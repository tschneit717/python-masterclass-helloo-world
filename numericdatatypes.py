# integers are faster than floats when computing
# There is no int limit in python
# Floating point nums are slower
# The max float val on a 64 bit comp is 1.79e+308 and
# the smallest is 2.22e-307

a = 12
b = 3
c = a * b
print(c + b)
print(c - a)
print(c % a)  # modulo: the remainder after an int division
print(c / a)  # float division
print(c // a)  # int division, rounded down towards minus infinity
print(c / a == 0)

print()

# for i in range(1, a / b):  <<-- this will fail, as it is a float. For in range needs an int
for i in range(1, 4):
    print(i)


# Expressions are anything that can be calculated to a value
# we bind/attach variables to values
