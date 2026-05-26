import pandas as pd


data = {
    'Name': ['Alice','Bob','Carol','David', 'Eve'],
    'Age': [22, 35,34,34, 76],
    'Grade': [86, 83,25,64,74],
    'Passed': [True, True, False, False, True]
}

df = pd.DataFrame(data)

print("--DF--")
print(df)
print("-----")

print("--Head--")
print(df.head())
print("-----")

print("--Head(3)--")
print(df.head(3))
print("-----")

print("--Shape--")
print(df.shape)
print("-----")

print("--info--")
print(df.info())
print("-----")

print("--describe--")
print(df.describe())
print("-----")

print("--columns--")
print(df.columns)
print("-----")