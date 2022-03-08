import numpy as np
A = np.random.randint(3,size=(6))
B = np.random.randint(3,size=(6))
print(A)
print(B)
comparison = A==B
equal_arrays = comparison.all()
print(equal_arrays)
