# Problem 3
import tabulate

# creating empty list
lt = []

# 3a
# adding rows into list
lt.append([1,"Akash",93])
lt.append([2,"Bhargav",87])
lt.append([3,"Chanakya",75])
lt.append([4,"Diksha",85])

# Printing them in tabular form

# using for loop
hd=['Rollno','Name','   Marks']
print(hd[0],hd[1],hd[2])
for i in range(len(lt)):
    print(lt[i][0],'    ',lt[i][1],'  ',lt[i][2])

print()
# using formatting
print('%-6s %-10s %-5s' % ("Rollno", "Name", "Marks"))
for i in range(len(lt)):
    print('%-6i %-10s %-5i' % (lt[i][0],lt[i][1],lt[i][2]))


# using tabulate module
print(tabulate.tabulate(lt,headers=hd,tablefmt="grid"))

#b
print('~3b~')
for i in range(3):
    print(lt[1][i],end='  ')