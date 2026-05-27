import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
print(f'Data {df.shape}')
print(df.describe().T.to_string())
print(f'\nHow many missing values is columns:\n{df.isna().sum()}')

# everywhere, where 0 and N/A put average for column
for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col] = df[col].replace(0, np.nan)
    mean_ = df[col].mean()
    df[col] = df[col].replace(np.nan, mean_)

print(f'\nAfter fixing:\nHow many missing values is columns:\n{df.isna().sum()}')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X =      # inputs
y =      # outputs
#tran test split

model = LogisticRegression()
# fit the model, show results
