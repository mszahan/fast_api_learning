import numpy as np

l = np.array([1, 2, 3])
m = np.array([4, 5, 6])

# adding two array
print('adding two array', l + m)

# mulitplies each element with the number
print('adding array with number',  l*2)

# mulitply two array
print('multiply two array', l*m)

# adding 1x3 array with 4x3
# the one row of 1x3 adds to the every row of 4x3 array
# you can not add a 1x 4 array to 4x3 array though
a1 = np.ones((4, 3))
a2 = np.ones((1, 3))
print('adding 1x3 with 4x3 array: ', a1+a2)

# Aggregating arrays - sum, min, max, mean

two_dim = np.random.randint(10, size=(3, 4))
print('3x4 random array', two_dim)
print('mean of the array: ', two_dim.mean())
print('min of the array: ', two_dim.min())
print('max of the array', two_dim.max())
print('sum of the array elements', two_dim.sum())


# comparing array
# return bool value for each element
l = np.array([1, 2, 3, 4])
print('comparing each element:', l < 3)

print('comparing array with array', two_dim <= np.array([1, 5, 9, 13]))
