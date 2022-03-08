import numpy as np
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
V = np.arange(a,b+1)
print(V)
nz=int(input("enter the no. of zeros interleaved: "))
Z0 = np.zeros(len(V) + (len(V)-1)*(nz))

Z0[::nz+1]=V
print()
print(Z0)
