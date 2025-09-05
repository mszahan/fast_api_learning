import numpy as np

l = np.arange(5)
print('whole array', l)
print('third element of the array', l[2])

# accessing series of elemnts
print('slicing the array:', l[1:4])

# every second elements of the array
print('every second element', l[::2])

# accessing two dimentional array
np.random.seed(0)
m = np.random.randint(10, size=(3, 4))
print('the array:', m)
print('element of second row third column', m[1][2])

# assaigning new element
m[1][2] = 42
print('updated array', m)

print('from rwo 1 to end and column 0 to 2', m[1:, 0:2])
print('every row, only last column', m[::, 3:])

shallow_copy = m[::, 3:]

# if you change the value of shallow copy...
# it will also change the main array value
shallow_copy[0][0] = 65
print('shallow copy', shallow_copy)
print('main array also changed', m)

# to avoid the issue you need to do actual copy
actual_copy = m[::, 3:].copy()
actual_copy[0][0] = 95
print('actual copy', actual_copy)
print('main array did not change', m)
