import pandas as pd

grades_with_index = pd.Series([85, 92, 96, 36,79])

print(grades_with_index)

grades_with_name = pd.Series([85, 92, 96, 36,79], index=['Alice', 'Bob', 'Carol','David', 'Eve'])

print('-------')
print(grades_with_name)

print(grades_with_name['Alice'])