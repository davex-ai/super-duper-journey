
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
# print(df["score"].max())
# print(df["age"].min())


# print the first 3 rows
# print only the name column
# print students with score > 85
# print students with age >= 18
# add a new column called passed where score >= 50
# print the average score
# print only name and score columns
# print the row for Mary

print(df[:3])
print(df['name'])
print(df['score'] > 85)
print(df['age'] >= 18)
df['passed'] = df['score'] >= 50
print(df['score'].mean())
print(df[['score' ,'name']])
print(df[df['name'] == 'Mary'])
