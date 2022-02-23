# Problem 4

# User input
inp = input("Enter the number to be checked: ")

# reversing the given input
rev = inp[::-1]
if int(inp) == int(rev):
    print('True')
else:
    print('False')
