import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weight-height.csv', sep=';')
print(df)

# df['Height'] = df['Height'] * 2.54
df['Height'] *= 2.54
df['Weight'] /= 2.2
df['BMI'] = df['Weight'] / (df['Height'] ** 2) * 10000
df['Extra'] = df['Weight'] + 67   # add column
del df['Extra']  # delete column
print(df)
print(df.describe().T.to_string())

plt.hist(df.query("Gender=='Female'")['Weight'], bins=30)
plt.hist(df.query("Gender=='Male'")['Weight'], bins=30)
plt.show()
plt.scatter(df['Weight'],df['Height'])
plt.show()
print('How many men and how many women')
print(df['Gender'].value_counts())
print('New scatter for men and women')
plt.scatter(df.query("Gender=='Female'")['Weight'] , df.query("Gender=='Female'")['Height'])
plt.scatter(df.query("Gender=='Male'")['Weight'] , df.query("Gender=='Male'")['Height'])
plt.show()
plt.hist(df.query("Gender=='Female'")['BMI'], bins=50)
plt.hist(df.query("Gender=='Male'")['BMI'], bins=50)
plt.show()


