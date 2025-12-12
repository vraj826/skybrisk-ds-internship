# Pandas: Handling missing values

import pandas as pd

df = pd.DataFrame({
    "A": [10, None, 30],
    "B": [5, 15, None]
})

clean_df = df.dropna()

print("Original DataFrame:\n", df)
print("\nAfter Dropping NaN:\n", clean_df)
