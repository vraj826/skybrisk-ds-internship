import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

df = pd.read_csv("data.csv")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)

print("Selected Feature Shape:", X_selected.shape)
