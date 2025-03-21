import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create 'Salary' dataset
data = {
    'Age': np.random.randint(20, 60, 100),
    'YearsExperience': np.random.randint(1, 40, 100),
    'EducationLevel': np.random.randint(1, 5, 100),
    'Salary': np.random.randint(30000, 150000, 100)
}
salary_df = pd.DataFrame(data)

# Identify independent and target variables
X = salary_df[['Age', 'YearsExperience', 'EducationLevel']]
y = salary_df['Salary']

# Split the data into training and testing sets (70/30 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print training and testing sets
print("Training set:")
print(pd.concat([X_train, y_train], axis=1))

print("\nTesting set:")
print(pd.concat([X_test, y_test], axis=1))

# Build and train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict salaries on the test set
y_pred = model.predict(X_test)
print("\nPredicted salaries:", y_pred)
