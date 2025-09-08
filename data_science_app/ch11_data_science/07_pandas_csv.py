import pandas as pd

museums = pd.read_csv('museums.csv', index_col=0)

print('data from csv file\n', museums)

# creating new csv file from the dataframe
museums['total'] = museums['paid'] + museums['free']
museums.to_csv('museum_total.csv')
