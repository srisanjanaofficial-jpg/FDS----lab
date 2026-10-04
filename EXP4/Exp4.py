
    import pandas as pd
import matplotlib.pyplot as plt

# LINE PLOT

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Name', 'Age', 'Marks']

df = pd.read_csv('student.csv', names=headers)

df.set_index('Name').plot()

plt.show()


# BAR PLOT

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.bar(X, Y, color='g')

plt.title("Students over 11 Years")
plt.show()


# HISTOGRAM

data = pd.read_csv('diabetes.csv')

plt.hist(data['Glucose'])

plt.xlabel("Glucose")
plt.ylabel("Frequency")

plt.title("Histogram")

plt.show()


# DENSITY PLOT

data = pd.read_csv('diabetes.csv')

data['Glucose'].plot.density()

plt.title("Density Plot")

plt.show()


# SCATTER PLOT

data = pd.read_csv('Cricketers2.csv')

plt.scatter(
    data.iloc[:, 0],
    data.iloc[:, 1]
)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Scatter Plot")

plt.show()