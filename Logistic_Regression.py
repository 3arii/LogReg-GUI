import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv("finalPrimeData.csv")

X = df.iloc[:, 1:].values  # bağımsız değişkenler
Y = df.iloc[:, 0]. values  # bağımlı değişkenler

testElem = X[len(X) - 1]
testElem = np.reshape(testElem, (-1, 5))

X_egitim, X_test, Y_egitim, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=0)

sc = StandardScaler()
X_egitim = sc.fit_transform(X_egitim)
X_test = sc.fit_transform(X_test)
testElem = sc.fit_transform(testElem)


def modeller(X_egitim, Y_egitim):

    log = LogisticRegression(random_state=0)
    log.fit(X_egitim, Y_egitim)

    #print("[0]Logistic Regression Training Accuracy:",
    #     log.score(X_egitim, Y_egitim))

    return log


model = modeller(X_egitim, Y_egitim)

cm = confusion_matrix(Y_test, model.predict(X_test))

TP = cm[1][1]
TN = cm[0][0]
FN = cm[1][0]
FP = cm[0][1]

global pred
pred = model.predict(testElem)
