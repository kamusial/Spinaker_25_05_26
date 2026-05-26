import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weight-height.csv', sep=';')
print(df)

# df['Height'] = df['Height'] * 2.54
df['Height'] *= 2.54
df['Weight'] /= 2.2
df['BMI'] = df['Weight'] / (df['Height'] ** 2) * 10000
print(df)
print(df.describe().T.to_string())

plt.hist(df.query("Gender=='Female'")['Weight'], bins=30)
plt.hist(df.query("Gender=='Male'")['Weight'], bins=30)
plt.show()




