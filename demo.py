import pandas as pd

df = pd.read_csv('D://Video//reshape//1.csv')
df = pd.DataFrame(df).set_index('country')
print(df)
df = df.reset_index()
df1 = df.melt(
    id_vars = ['country'],
    #value_vars=['year'],
    var_name = 'year',
    value_name = 'cases'
).dropna()
df1 = df1.sort_values(by = "year")
print(df1)
df1.to_csv('test.csv', index = False)