import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create User Data (Age vs Income)
data = {
    'Age': [18, 20, 22, 25, 28, 30, 35, 40, 45, 50],
    'Income': [15000, 18000, 22000, 25000, 30000, 32000, 40000, 45000, 50000, 55000]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Define Independent (X) and Target (Y) Variables
X = df[['Age']]  # Independent Variable (Feature)
Y = df['Income']  # Target Variable

# Split Data into Training and Testing Sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make Predictions
Y_pred = model.predict(X_test)

# Visualize the Results (Training Set)
plt.scatter(X_train, Y_train, color='blue')
plt.plot(X_train, model.predict(X_train), color='red')
plt.title('Age vs Income (Training Set)')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

# Visualize the Results (Test Set)
plt.scatter(X_test, Y_test, color='green')
plt.plot(X_train, model.predict(X_train), color='red')
plt.title('Age vs Income (Test Set)')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

# Evaluate Model Performance
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R2 Score:", r2_score(Y_test, Y_pred))
