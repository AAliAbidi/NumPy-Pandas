import numpy as np
ary1 = np.array([1, 2, 3])
ary2 = np.array([2, 3, 4])
dot = 0
for i, j in zip(ary1, ary2):
    dot += i*j
print(dot)

# using numpy
dot2 = ary1*ary2
print("Vector \n", dot2)

# using numpy sum
print("Sum is \n", sum(ary1*ary2))

# another way
print("", (ary1*ary2).sum())

# using numpy inbuilt DOT function
print("", np.dot(ary1, ary2))

# we can also do
print("", ary1.dot(ary2))
print("", ary2.dot(ary1))

# calculating magnitude
print("Magnitude: ", np.sqrt((ary1*ary1).sum()))

# linalg inbuilt functions
print("Magnitude: ", np.linalg.norm(ary1))

# calculating angle
cosinangle = ary1.dot(ary2) / (np.linalg.norm(ary1) * np.linalg.norm(ary2))
print("Cosangle:  ", cosinangle)
# Radian angle
angle = np.arccos(cosinangle)
print("Angle RAD: ", angle)







