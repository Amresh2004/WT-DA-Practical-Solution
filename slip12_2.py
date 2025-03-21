import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create 'heights-and-weights' dataset
data = {
    'Height': [150, 160, 165, 170, 175, 180, 185, 190, 195, 200],
    'Weight': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Purchases': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

heights_weights_df = pd.DataFrame(data)

# Display dataset information
print("Dataset Information:")
print(heights_weights_df.info())

# Identify independent and target variables
X = heights_weights_df[['Height', 'Weight']]
y = heights_weights_df['Purchases']

# Split data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print the shapes of training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Build simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Make predictions
predictions = model.predict(X_test)
print("Predictions on test set:", predictions)
