import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(df.head())
df = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
print(df.columns)
# df.info()
# print(df.describe())
# print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
# print(model.score(X_test, y_test))
importance = pd.Series(model[1].coef_[0], index=X.columns)
# print(importance.sort_values(ascending=False))
cm = confusion_matrix(y_test, y_pred)
# [[TN, FP], [FN, TP]]
print(cm)
# Precision = TP / (TP + FP)
precision = cm[1, 1] / (cm[1, 1] + cm[0, 1])
# Recall = TP / (TP + FN)
recall = cm[1, 1] / (cm[1, 1] + cm[1, 0])
print("Recall:", recall)
print("Precision:", precision)

print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

scores = cross_val_score(model, X, y, cv=5)# cv=5 is doing what? why did we put raw x and not x_train and y train

print("CV Scores:", scores)
print("Average:", scores.mean())

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

print("RF Accuracy:", rf.score(X_test, y_test))