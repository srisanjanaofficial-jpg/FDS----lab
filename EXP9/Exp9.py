
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import io
import requests

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix
)

import seaborn as sns


# CSV file URL

dataURL = "http://www.ats.ucla.edu/stat/data/binary.csv"


# Get CSV content

getCSV = requests.get(dataURL).content


# Load dataset

dataset = pd.read_csv(
    io.StringIO(
        getCSV.decode('utf-8')
    )
)


# Display dataset information

print(type(dataset))

print(dataset.head())

print(dataset.shape)

print(dataset.info())

print(dataset.count())

print(dataset.columns)


# Visualization

sns.pairplot(
    dataset,
    hue='admit'
)

plt.show()


# Convert DataFrame into matrix

dataArray = dataset.values

X = dataArray[:, 1:4]

y = dataArray[:, 0:1]


# Split dataset

validation_size = 0.10
seed = 9

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    y,
    test_size=validation_size,
    random_state=seed
)


# Models

num_trees = 200
max_features = 3

models = []

models.append(
    ('LR', LogisticRegression())
)

models.append(
    ('LDA', LinearDiscriminantAnalysis())
)

models.append(
    ('KNN', KNeighborsClassifier())
)

models.append(
    ('CART', DecisionTreeClassifier())
)

models.append(
    (
        'RF',
        RandomForestClassifier(
            n_estimators=num_trees,
            max_features=max_features
        )
    )
)

models.append(
    ('NB', GaussianNB())
)

models.append(
    ('SVM', SVC())
)


# Evaluate models

results = []
names = []

scoring = 'accuracy'

kfold = KFold(
    n_splits=10,
    shuffle=True,
    random_state=seed
)

for name, model in models:

    cv_results = cross_val_score(
        model,
        X_train,
        Y_train.ravel(),
        cv=kfold,
        scoring=scoring
    )

    results.append(cv_results)
    names.append(name)

    print(
        "%s: %f (%f)" %
        (
            name,
            cv_results.mean(),
            cv_results.std()
        )
    )


# Logistic Regression model

model = LogisticRegression()

model.fit(
    X_train,
    Y_train.ravel()
)


# Predictions

predictions = model.predict(X_test)


# Accuracy

accuracy = accuracy_score(
    Y_test,
    predictions
)

print("Accuracy:", accuracy)


# Confusion Matrix

cm = confusion_matrix(
    Y_test,
    predictions
)

print("Confusion Matrix:")
print(cm)


# Heatmap

sns.heatmap(
    cm,
    annot=True,
    fmt='d'
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()


# New predictions

new_data = np.array([
    [720, 4, 1],
    [300, 2, 1],
    [400, 4, 4]
])

new_predictions = model.predict(
    new_data
)

print("Predictions:")

for prediction in new_predictions:

    if prediction == 1:
        print("ADMIT")
    else:
        print("REJECT")