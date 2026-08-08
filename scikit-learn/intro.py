from pyexpat import features

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import importlib.util

from sklearn.tree import DecisionTreeRegressor

file_path = r'C:\Users\DELL\PycharmProjects\ML\pandas-learn\student-performance_analysis.py'

# Load the module dynamically
spec = importlib.util.spec_from_file_location("student_analysis", file_path)
student_analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student_analysis)
df = student_analysis.df
X = df[['attendance', 'math_score', 'english_score']]      # input (feature)
y = df['avg_score']         # output (target)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
# print(df.head())
lrmodel = LinearRegression()
lrmodel.fit(X_train, y_train)

dtmodel = DecisionTreeRegressor(max_depth=5)
dtmodel.fit(X_train, y_train)

rfmodel = RandomForestRegressor()
rfmodel.fit(X_train, y_train)

models = {
    'LinearRegression': lrmodel,
    'DecisionTreeRegressor': dtmodel,
    'RandomForestRegressor': rfmodel
}

for name, model in models.items():
    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    print(name, "MSE:", mse)

importance = rfmodel.feature_importances_
features = X.columns
print(pd.DataFrame({'feature': features, 'importance': importance}).sort_values(by='importance', ascending=False))
# y_pred = model.predict(X_test)
# print("Prediction:", y_pred)
# print("Actual Value:", y_test.values)
