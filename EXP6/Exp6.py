
import pandas as pd
import numpy as np
import statistics as st
from scipy.stats import iqr

df = pd.DataFrame({
    'ID': ['1', '2', '3', '4', '5'],
    'Name': ['CS', 'SE', 'SE', 'SE', 'CS'],
    'Department': ['cse', 'eee', 'ece', 'it', 'AI'],
    'Year': ['3', '2', '1', '4', '1'],
    'Subject_Marks': [72, 73, 72, 72, 73]
})

display(df)

dataMatrix = {
    "Subject_Marks": [72, 73, 72, 72, 73]
}

dataFrame = pd.DataFrame(data=dataMatrix)

print("DataFrame:")
print(dataFrame)

# Mean
print("Mean: Computed column-wise:")

meanData = dataFrame.mean()

print(meanData)

print("Mean: Computed row-wise:")

meanData = dataFrame.mean(axis=1)

print(meanData)

# Median
print("Median: Computed column-wise:")

medianData = dataFrame.median()

print(medianData)

print("Median: Computed row-wise:")

medianData = dataFrame.median(axis=1)

print(medianData)

# Mode
print("Mode: Computed column-wise:")

modeData = dataFrame.mode()

print(modeData)

print("Mode: Computed row-wise:")

modeData = dataFrame.mode(axis=1)

print(modeData)

# Standard deviation
print("Standard Deviation:")

print(dataFrame.std())

# Variance
print("Variance:")

print(dataFrame.var())

# Interquartile Range
print("Interquartile Range:")

print(iqr(dataFrame['Subject_Marks']))

# Description
print(dataFrame.describe(include='all'))