import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. downloading data

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

try:
    df = pd.read_csv(url)
    print('data downloaded')
except Exception as e:
    print(f'Error {e}')
    print('Using backup data')
    data = {
        'name': ['IPA','IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Ale', 'Bock'],
        'alcohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],
        'bitterness': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],
        'rating': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
        'style': ['IPA', 'IPA', 'Lager', 'Dark', 'Lager', np.nan, 'Dark', 'Light', 'Dark']
    }
    df = pd.DataFrame(data)

# 2. Basic info
print('\n' + '='*50)
print(f'Data dimensions: {df.shape}')
print(f'Number of rows: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')

# 3. Data preview
print('First 5 beers')
print(df.head())
print('Last 3 beers')
print(df.tail(3))

# 4. Data types
print(f'\n{df.info()}')

# 5. Numerical statistics
numeric_columns = df.select_dtypes(include='number').columns   # names of numerical columns
if len(numeric_columns) > 0:
    print('Statistics for numerical features:')
    print(df[numeric_columns].describe().T.to_string())
else:
    print('No numerical columns in the data')

# 6. Categorical statistics
print("\n" + "="*50)
print("CATEGORICAL STATISTICS")
print("="*50)

text_columns = df.select_dtypes(include='str').columns
if len(text_columns) > 0:
    for column in text_columns:
        print(f'\nColumn: {column}')
        print(f'Number of unique values: {df[column].unique()}')
        print('3 most frequent values')
        print(df[column].value_counts().head(3))
else:
    print('No categorical columns in the data')

# 7. Missing values
print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)

missing_values = df.isnull().sum()
if missing_values.sum() > 0:
    print('Columns with missing values:')
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            missing_count = df[column].isnull().sum()
            missing_percentage = missing_count / len(df) * 100
            print(f'    {column}: {missing_count} ({missing_percentage:.1f})%')

# 8. Visualizations
print("\n" + "=" * 50)
print("CREATING CHARTS")
print("=" * 50)

# chart 1, alcohol content distribution
if 'alcohol' in df.columns and False:
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1) # one row, 2 columns, first from the left
    df['alcohol'].hist(bins=10, color='lightblue', edgecolor='black')
    plt.title('Alcohol content distribution')
    plt.xlabel('Alcohol content in (%)')
    plt.ylabel('Number of beers')
    plt.subplot(1, 2, 2)   # on the right
    df.boxplot(column='alcohol', grid=False)
    plt.title('Boxplot: Alcohol content')
    plt.tight_layout()
    plt.show()

# chart 2, rating distribution
if 'rating' in df.columns and False:
    plt.figure(figsize=(8, 5))
    df['rating'].hist(bins=8, color='lightgreen', edgecolor='black', alpha=0.7)
    plt.title('Beer rating distribution')
    plt.xlabel('Rating (on a scale from 1 to 5)')
    plt.ylabel('Number of beers')
    plt.grid(axis='y', alpha=0.3)
    plt.show()

# Chart 3: Relationship between alcohol and rating
if 'alcohol' in df.columns and 'rating' in df.columns and False:
    plt.figure(figsize=(8, 6))
    plt.scatter(df['alcohol'], df['rating'], alpha=0.6, s=60, color='purple')
    plt.title('Relationship between alcohol content and rating')
    plt.xlabel('Alcohol content (%)')
    plt.ylabel('Rating')
    plt.grid(True, alpha=0.3)
    # trend line
    z = np.polyfit(df['alcohol'], df['rating'], 1)
    p = np.poly1d(z)
    plt.plot(df['alcohol'], p(df['alcohol']), "r--", alpha=0.8)
    plt.show()

# Chart 4: Popularity of beer styles
if 'style' in df.columns and False:
    plt.figure(figsize=(10, 6))
    df['style'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
    plt.title('Popularity of beer styles')
    plt.xlabel('Beer style')
    plt.ylabel('Number of beers')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

# Chart 5: Correlation matrix (if there are at least 2 numerical columns)
if len(numeric_columns) >= 2:# and False:
    plt.figure(figsize=(8, 6))
    correlation_matrix = df[numeric_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlations between numerical features')
    plt.tight_layout()
    plt.show()

# Summary
print("\n" + "="*50)
print("ANALYSIS SUMMARY")
print("="*50)
print("EDA analysis completed successfully!")
print(f"Analyzed {len(df)} beers")
print(f"Number of features: {len(df.columns)}")

if len(numeric_columns) > 0:
    print("Found numerical features:", list(numeric_columns))
if len(text_columns) > 0:
    print("Found categorical features:", list(text_columns))

# highest rated
if 'rating' in df.columns and 'name' in df.columns:
    print("\n3 highest rated beers")
    best = df.nlargest(3, 'rating')[['name', 'rating']]
    print(best)

# highest alcohol content
if 'alcohol' in df.columns and 'name' in df.columns:
    print("\n3 beers with the highest alcohol content:")
    strong = df.nlargest(3, 'alcohol')[['name', 'alcohol']]
    print(strong)

print("\n" + "="*50)