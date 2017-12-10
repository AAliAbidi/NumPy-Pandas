# Why NumPy array is preferred over traditional Python List
# Speed Factor <Process is Fast>

import numpy as np
lst = [1, 2, 3]
print(lst)

for i in lst:
    print(lst)

ary = np.array([1, 2, 3])
for j in ary:
    print(ary)

# append element to array
lst.append(4)
print("List after appending 4 \n")
for k in lst:
    print(lst)

lst = lst+[5]   # another way of appending
print("List after appending 5 \n")
print(lst)

# ary.append(4) it will not work
# print(ary) not going to work
# arry += arry[4,5] not going to workk
# array addition
l2 = []
for e in lst:
    l2.append(e + e)
print(l2)

# trying in NumPy
print("NumPy makes calculation easy")
print(ary+ary)

# vector Multiplication
print("vector Multiplication")
print(2*ary)
print(2*lst)
# further calculation
# lst ** 2 it will not work we have to use loop
print("Further calculations")
lst3 = []
for e in lst:
    lst3.append(e*e)
print(lst3)
# But it is easy using numPy
print(ary**2)

print("Square Root")
print(np.sqrt(ary))
print("log")
print(np.log(ary))
print("Exponential")
print(np.exp(ary))


