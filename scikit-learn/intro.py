from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import importlib.util


file_path = r'C:\Users\DELL\PycharmProjects\ML\pandas-learn\student-performance_analysis.py'

# Load the module dynamically
spec = importlib.util.spec_from_file_location("student_analysis", file_path)
student_analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student_analysis)
df = student_analysis.df
X = df[['attendance']]      # input (feature)
y = df['avg_score']         # output (target)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print(df.head())
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
mse = mean_squared_error(y_test, y_pred)
print(mse)