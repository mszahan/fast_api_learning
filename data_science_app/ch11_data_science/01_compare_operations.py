import numpy as np

np.random.seed(0)

m = np.random.randint(10, size=1000000)


def standard_double(array):
    output = np.empty(array.size)
    for i in range(array.size):
        output[i] = array[i] * 2
    return output


double = standard_double(m)

print(double)


def numpy_double(array):
    return array*2


# it takes significantly less time than the previous one (250 times faster)
num_double = numpy_double(m)
print(num_double)
