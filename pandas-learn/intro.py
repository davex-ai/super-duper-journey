
import pandas as pd

data = {
    "name": ["Dave", "Ada", "John", "Mary", "Paul"],
    "age": [15, 18, 21, 17, 19],
    "score": [90, 85, 88, 72, 95]
}

df = pd.DataFrame(data)
# print(df)

# print(df.head())      # first 5 rows
# print(df.tail())      # last 5 rows
# print(df.shape)       # (rows, columns)
# print(df.columns)     # column names
# print(df.info())      # data types and nulls
# print(df.describe())  # summary statistics
# print(df["name"].describe( ))  # summary statistics
# print(df["name"])
# print(df[["name", "score"]])
# print(df.iloc[0])      # first row by position
# print(df.iloc[0:2])
# print(df[df["age"] > 16])
# print(df[df["score"] >= 88])
# df["passed"] = df["score"] >= 50
# print(df)
# print(df["score"].mean())
# print(df["score"].max())
# print(df["age"].min())


