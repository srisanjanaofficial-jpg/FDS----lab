import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

# String array
arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype)

# Array with string datatype
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)

# Array using arange()
arr = np.arange(0, 10, 2)
print(arr)

# Random integer array
arr = np.random.randint(1, 10, 5)
print(arr)

# Random floating-point array
arr = np.random.rand(5)
print(arr)

# Indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[2])

# Slicing
print(arr[1:4])

# Reshaping
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = arr.reshape(2, 3)
print(newarr)

# Joining arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

# Splitting arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Universal function
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.add(arr1, arr2)
print(newarr)

# Check ufunc
print(type(np.add))

if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")

# Mathematical functions
x = np.arange(0, 1.25, 0.25)
print(x)

y = np.sin(2 * np.pi * x)
print(y)

# Convert degrees to radians
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# Find angle
x = np.arcsin(1.0)
print(x)

# CSV operations
import csv

with open("winequality-red.csv", 'r') as f:
    wines = list(csv.reader(f, delimiter=";"))

wines = np.array(wines[1:], dtype=float)

print(wines)

# Mean
print(np.mean(wines, axis=0))

# Median
print(np.median(wines, axis=0))

# Maximum
print(np.max(wines, axis=0))

# Minimum
print(np.min(wines, axis=0))

# Comparison operation
print(wines[:, 11] > 5)

# Quality equal to 10
print(wines[:, 11] == 10)

# Select wines with quality above 7
high_quality = wines[:, 11] > 7
print(wines[high_quality, :][:3, :])