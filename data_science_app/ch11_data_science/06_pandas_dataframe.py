import pandas as pd

paid = {"Louvre Museum": 5988065, "Orsay Museum": 1850092,
        "Pompidou Centre": 2620481, "National Natural History Museum": 404497}

free = {"Louvre Museum": 4117897, "Orsay Museum": 1436132,
        "Pompidou Centre": 1070337, "National Natural History Museum": 344572}

museums = pd.DataFrame({'paid': paid, 'free': free})

print(museums)
print('the index: ', museums.index)

print('accessing value with key\n', museums['free'])

print('accessing data by slicing through keys\n',
      museums['Louvre Museum':'Orsay Museum'])

print('accessing data with slcing and key\n',
      museums['Louvre Museum':'Orsay Museum']['paid'])

# adding new column by addition of two column
museums['total'] = museums['paid'] + museums['free']
print(museums)


print('sum of the total column:', museums['total'].sum())
print('mean of the total column', museums['total'].mean())
