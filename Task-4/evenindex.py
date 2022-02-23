# Problem2

# input from user
wrd = str(input("Enter the string: "))

# getting length of the string using len function
ln = len(wrd)
print()
# using slicing output is given
print("The characters at even indexes are: ", wrd[0:ln:2])
