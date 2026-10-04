
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Ungrouped frequency distribution

df = pd.DataFrame({
    'ID': ['1', '2', '3', '4', '5', '6'],
    'Product_name': [
        'alex', 'bob', 'cathy',
        'doge', 'eric', 'fred'
    ],
    'State': [
        'Taminadu',
        'Tamilnadu',
        'Taminadu',
        'Andra',
        'Madhyapradesh',
        'Orissa'
    ],
    'Salescount': [
        '1000',
        '2000',
        '3500',
        '450',
        '560',
        '250'
    ]
})

print(df)

plt.hist(df['State'])

plt.ylabel('Frequency count')
plt.xlabel('Data')
plt.title('My histogram')

plt.show()


# Grouped frequency distribution

df = pd.DataFrame({
    'ID': ['1', '1', '2', '3', '4'],
    'Product_Name': [
        'CS', 'SE', 'SE', 'SE', 'CS'
    ],
    'State': [60, 70, 59, 51, 80],
    'Salescount': [20, 21, 20, 22, 23]
})

display(df)

df.groupby('ID')['Salescount'].max().plot(
    kind='bar',
    legend=True
)

plt.show()


# Cumulative frequency distribution

Salescount = [20, 21, 20, 22, 23]

a, b, c, d = stats.cumfreq(
    Salescount,
    numbins=4
)

print("cumulative frequency :", a)
print("Lower Limit :", b)
print("bin size :", c)
print("extra-points :", d)


# Relative frequency distribution

fig = plt.figure()

ax = fig.add_subplot(111)

ax.hist(
    Salescount,
    edgecolor='black',
    weights=np.ones_like(Salescount) /
            len(Salescount)
)

plt.show()