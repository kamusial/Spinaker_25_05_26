import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
print(f'Data {df.shape}')
print(df.describe().T.to_string())
print(f'\nHow many missing values is columns:\n{df.isna().sum()}')

# everywhere, where 0 and N/A put average for column