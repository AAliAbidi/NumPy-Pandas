# Matrix is 2or 3 Dimensional array
import numpy as np
M = np.array([[1, 2, 3], [2, 4, 5]])
L = [[4, 5, 6], [10, 11, 10]]
print("M\n", M)
print("L\n", L)
print("M\n", M[0])
print("L\n", L[0])
print("M\n", M[(0, 0), (0, 1)])

M2 = np.matrix([[1, 2, 3], [4, 5, 6]])
print("M2\n", M2)

print("Getting Matrix as an array\n")
ary = np.array(M2)
print(ary)

print("Transpose of matrix\n", M2.T)
print("We can also perform this action with array\n", ary.T)


