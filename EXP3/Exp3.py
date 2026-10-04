
import pandas as pd

# Read CSV
data = pd.read_csv("employees.csv")

# Check NULL values
bool_series = pd.isnull(data["Team"])
print(data[bool_series])

# Check NOT NULL values
bool_series = pd.notnull(data["Gender"])
print(data[bool_series])

# Drop rows containing NULL values
new_data = data.dropna(axis=0, how='any')
print(new_data)

# Fill missing values
data["Team"] = data["Team"].fillna("Unknown")
print(data)

# Apply function
data["Salary"] = data["Salary"].apply(
    lambda x: x * 2
)

print(data)

# Map function
data["Gender"] = data["Gender"].map(
    lambda x: x.upper() if isinstance(x, str) else x
)

print(data)

# Detect outliers
print(data.describe())

# Vectorized string operations
data["First Name"] = data["First Name"].str.upper()
print(data)

data["Gender"] = data["Gender"].str.lower()
print(data)