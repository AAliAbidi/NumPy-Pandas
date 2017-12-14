import numpy as np

ary = np.array([[1, 2, 3], [2, 3, 4]])
print(ary)
print("\n", ary)

Z = np.zeros(10)
print("Z\n",Z)

Z2 = np.zeros((10, 10))

print("Z2\n", Z2)

Z3 = np.ones((10, 10))

print("Z3\n", Z3)

Z4 = np.random.random((10, 10))

print("Z4\n", Z4)

print("******GAUSSIAN*******")

Z5 = np.random.randn(10, 10)
print("Z5\n", Z5)

print("means\n", Z5.mean())
print("Variance\n", Z5.var())
