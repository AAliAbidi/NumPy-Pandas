# Practice Code for matrix and linear algebra
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
Ainv = np.linalg.inv(A)
print(Ainv)

print(Ainv.dot(A))

print(A.dot(Ainv))

Det = np.linalg.det(A)
print(Det)

print(np.diag(A))

# Outer Product
j = np.array([1, 2])
B = np.array([3, 4])

print(np.outer(j, B))

# Inner product
print(np.inner(j, B))

r = np.diag(j).sum()
Q = np.trace(j)
print(r)
print(Q)

# linear algebra
ary1 = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
c = np.linalg.inv(ary1).dot(b)
print(c)
print(np.linalg.solve(ary1, b))

# solving problem based on documentation
g = np.array([[1, 1], [1.5, 4]])
h = np.array([2200, 5050])
w = np.linalg.solve(g, h)
print(w)



