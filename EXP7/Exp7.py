
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('Marks.csv')


def UVA_numeric(data):

    var_group = data.columns
    size = len(var_group)

    plt.figure(
        figsize=(7 * size, 3),
        dpi=400
    )

    for j, i in enumerate(var_group):

        mini = data[i].min()
        maxi = data[i].max()

        ran = data[i].max() - data[i].min()

        mean = data[i].mean()
        median = data[i].median()

        st_dev = data[i].std()

        skew = data[i].skew()
        kurt = data[i].kurtosis()

        points = mean - st_dev, mean + st_dev

        plt.subplot(
            1,
            size,
            j + 1
        )

        sns.distplot(
            data[i],
            hist=True,
            kde=True
        )

        sns.lineplot(
            points,
            [0, 0],
            color='black',
            label="std_dev"
        )

        sns.scatterplot(
            [mini, maxi],
            [0, 0],
            color='orange',
            label="min/max"
        )

        sns.scatterplot(
            [mean],
            [0],
            color='red',
            label="mean"
        )

        sns.scatterplot(
            [median],
            [0],
            color='blue',
            label="median"
        )

        plt.xlabel(
            '{}'.format(i),
            fontsize=20
        )

        plt.ylabel('density')

        plt.title(
            'std_dev = {}; kurtosis = {};\n'
            'skew = {}; range = {}\n'
            'mean = {}; median = {}'.format(
                (
                    round(points[0], 2),
                    round(points[1], 2)
                ),
                round(kurt, 2),
                round(skew, 2),
                (
                    round(mini, 2),
                    round(maxi, 2),
                    round(ran, 2)
                ),
                round(mean, 2),
                round(median, 2)
            )
        )


UVA_numeric(df)


# Q-Q Plot

import numpy as np
import statsmodels.api as sm
import pylab as py

data_points = np.random.normal(
    0,
    1,
    100
)

sm.qqplot(
    data_points,
    line='45'
)

py.show()