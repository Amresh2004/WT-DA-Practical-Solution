import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create 'Position_Salaries' dataset
data = {
    'Position': ['Intern', 'Junior', 'Senior', 'Lead', 'Manager', 'Director', 'VP', 'SVP', 'C-level', 'CEO'],
    'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [15000, 25000, 50000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
}
position_salaries_df = pd.DataFrame(data)

# Identify independent and target variables
X = position_salaries_df[['Level']]
y = position_salaries_df['Salary']

# Split the data into training and testing sets (70/30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print training and testing sets
print("Training set:")
print(pd.concat([X_train, y_train], axis=1))

print("\nTesting set:")
print(pd.concat([X_test, y_test], axis=1))

# Build and train a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print coefficients
print("\nIntercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Test the model
y_pred = model.predict(X_test)
print("\nPredicted salaries:", y_pred)
