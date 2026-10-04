
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read Iris dataset

df = pd.read_csv("Iris.csv")

# Display first five rows

print(df.head())

# Shape

print(df.shape)

# Check null values

print(df.isnull().sum())

# Remove duplicate species

data = df.drop_duplicates(
    subset="Species"
)

print(data)

# Count species

print(df.value_counts("Species"))

# Count plot

sns.countplot(
    x='Species',
    data=df
)

plt.show()

# Correlation matrix

print(
    df.corr(
        numeric_only=True,
        method='pearson'
    )
)

# Correlation heatmap

corr = df.corr(
    numeric_only=True
)

sns.heatmap(
    corr,
    xticklabels=corr.columns.values,
    yticklabels=corr.columns.values
)

plt.show()