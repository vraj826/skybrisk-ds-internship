import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Sample Predictions:")
print(predictions[:5])
