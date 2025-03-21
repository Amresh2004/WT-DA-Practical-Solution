import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


car_data = {
    'Horsepower': [120, 130, 100, 150, 180, 110, 200, 170, 140, 160],
    'Price': [15000, 16000, 12000, 18000, 21000, 12500, 24000, 20000, 17500, 19000]
}

# Convert to DataFrame
df = pd.DataFrame(car_data)

# Display first few rows
print("Dataset Preview:\n", df.head())

# Split data into features (X) and target (y)
X = df[['Horsepower']]
y = df['Price']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Get the intercept and coefficient
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Make predictions
y_pred = model.predict(X_test)

# Compare predicted vs actual
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nPredicted vs Actual:\n", results)

# Visualize the results
plt.scatter(X_test, y_test, color='blue', label='Actual Price')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.legend()
plt.show()

# Evaluate the model
print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Test with a new horsepower value
new_hp = [[190]]
predicted_price = model.predict(new_hp)
print(f"Predicted price for {new_hp[0][0]} horsepower: ${predicted_price[0]:.2f}")