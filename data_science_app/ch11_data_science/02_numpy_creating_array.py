import numpy as np

list_of_nums = np.array([1, 2, 3, 4, 5])
print(list_of_nums)

# array with data type
float_nums = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print('float data type', float_nums)

# float number will be converted to int if added to array with int values
list_of_nums[0] = 13.32
print('added 13.32', list_of_nums)


# can't assign string to an array with integer
# will throw an error
# list_of_nums[0] = 'hola'

# list full with zeros
zeros = np.zeros(5)
print('list of zeros', zeros)

# list with ones
ones = np.ones(6)
print('list with ones', ones)

# empty list - will popluate with last use list elements
empty = np.empty(6)
print('empty list', empty)

# list with range or numbers
arange = np.arange(5)
print('list with arange', arange)


# list with random integer
np.random.seed(0)  # set the random seed to make examples reproducible
random_nums = np.random.randint(10, size=5)
print('list of 5 random numbers up to 10', random_nums)


# two dimentional list
two_dim_list = np.ones((3, 4))
print('two diemntional list 3x4', two_dim_list)
print('diemntion of the list: ', two_dim_list.ndim)
print('shape of the list: ', two_dim_list.shape)
print('size of the list: ', two_dim_list.size)
