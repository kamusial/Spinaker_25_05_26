import pandas as pd

data = {
    'Name': ['Alice','Bob','Carol','David', 'Eve'],
    'Age': [22, 35,38,34, 76],
    'Grade': [86, 83,25,64,74],
    'Passed': [True, True, False, False, True]
}

df = pd.DataFrame(data)

df_s = df[['Age', 'Passed' ]]

print(df_s)


df_first_step = df['Age'] > 36
print(df_first_step)

df_second_step = df[df['Age'] > 36]
print(df_second_step)

print(df[(df['Age'] > 36) & (df['Grade'] >= 70)])


df['Passed_second_column'] = df['Grade'] >= 50

print('---')
print(df)

df['Bonus'] = df['Grade'] * 0.5
print('---')
print(df)

print('mean')
print(df['Grade'].mean())
print('max')
print(df['Grade'].max())
print('min')
print(df['Grade'].min())
print('sum')
print(df['Grade'].sum())
print('value_counts')
print(df['Grade'].value_counts())
print('std')
print(df['Grade'].std())
