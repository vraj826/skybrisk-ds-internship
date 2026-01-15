import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print("Logistic Regression model trained successfully")
