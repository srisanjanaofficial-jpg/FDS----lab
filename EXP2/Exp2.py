
import pandas as pd
import matplotlib.pyplot as plt

# Creating a simple Series
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']

auth_series = pd.Series(author)

print(auth_series)

# Creating DataFrame using Series
article = [210, 211, 114, 178]

article_series = pd.Series(article)

frame = {
    'Author': auth_series,
    'Article': article_series
}

result = pd.DataFrame(frame)

age = [21, 21, 24, 23]

result['Age'] = pd.Series(age)

print(result)

# Import CSV file
df = pd.read_csv('winequality-red.csv')

# First 10 records
print(df.head(10))

# Last 10 records
print(df.tail(10))

# Shape
print(df.shape)

# Number of rows
print(df.shape[0])

# Number of columns
print(df.shape[1])

# Index
print(df.index)

# Columns
print(df.columns)

# Ranking
print(df.rank())

# Sorting
print(df.sort_values(by='quality'))

# Mean
print(df.mean(numeric_only=True))

# Median
print(df.median(numeric_only=True))

# Count
print(df.count())

# Unique values
print(df.nunique())

# Rename column
df.rename(
    columns={'quality': 'Quality'},
    inplace=True
)

print(df)