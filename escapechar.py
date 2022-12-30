print('escape me to a \nnew line')
tabline = '\tI have been indented in a new line'
print(tabline)
print("I need to escape \"these quotes\" and also \\ ")
print("""I learned that I ""can"" 'use' "triple" quotes""")

# You don't need to use escape chars in this example
anotherSplitString = """This string has been 
split over another
line"""

print(anotherSplitString)

print("C:\\Users\\tomschneider\\notes.txt")
print(r"C:\Users\tomschneider\notes.txt")