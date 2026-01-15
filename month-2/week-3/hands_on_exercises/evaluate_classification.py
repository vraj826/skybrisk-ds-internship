import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv("data.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)
precision = precision_score(y, predictions)
recall = recall_score(y, predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
