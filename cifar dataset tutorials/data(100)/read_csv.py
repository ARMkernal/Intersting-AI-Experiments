import pandas as pd 
datalist = pd.read_csv('classes.csv', dtype=str, encoding='utf-8', sep=',', header=None)

aquatic_mammals = datalist[0][0].values
fish = datalist[1:][1].values
print(aquatic_mammals)
