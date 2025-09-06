import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])

print('one dimentional series \n', s)

# get the type of series values
print('type of a series value: ', type(s.values))

# getting the elements with index
print('first element: ', s[0])
print('third element: ', s[2])

# getting elements by slice
print('slice the element with \n', s[1:3])

# creating series with custom index
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('series with custom index \n', s)

# accessing the value with the key
print('value of the c position:',  s['c'])

# slicing with the key
print('slicing the value fro key b:d \n', s['b': 'd'])
print('slicing with number though key are string \n', s[1:3])

# creating series with dictionary
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print('series from dictionary \n', s)
