import pandas as pd
brics = pd.read_csv('./brics.csv', index_col=0)
brics['added column'] = ['yes','no']
print brics

print 'all countries'
print brics['country']

print 'China'
print brics.loc['CH']