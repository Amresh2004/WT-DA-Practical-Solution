import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create 'nursery' dataset directly in the code
data = {
    'Parents': ['usual', 'pretentious', 'usual', 'usual', 'great_pret', 'usual', 'pretentious', 'great_pret'],
    'Has_nurs': ['proper', 'less_proper', 'improper', 'critical', 'proper', 'less_proper', 'critical', 'improper'],
    'Form': ['complete', 'complete', 'incomplete', 'foster', 'complete', 'complete', 'incomplete', 'foster'],
    'Children': ['1', '2', '3', 'more', '1', '2', '3', 'more'],
    'Housing': ['convenient', 'less_conv', 'critical', 'convenient', 'critical', 'less_conv', 'convenient', 'critical'],
    'Finance': ['convenient', 'convenient', 'inconv', 'convenient', 'inconv', 'convenient', 'inconv', 'inconv'],
    'Social': ['nonprob', 'slightly_prob', 'problematic', 'nonprob', 'slightly_prob', 'problematic', 'nonprob', 'slightly_prob'],
    'Health': ['recommended', 'priority', 'not_recom', 'recommended', 'priority', 'not_recom', 'recommended', 'priority'],
    'Purchases': [1, 0, 0, 1, 1, 0, 1, 0]
}

nursery_df = pd.DataFrame(data)

# Display dataset information
print("Dataset Information:")
print(nursery_df.info())

# Convert categorical data to numeric
nursery_df_encoded = pd.get_dummies(nursery_df.drop('Purchases', axis=1))

# Define independent and target variables
X = nursery_df_encoded
y = nursery_df['Purchases']

# Split data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print the shapes of training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Build a simple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Print coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Make predictions
predictions = model.predict(X_test)
print("Predictions on test set:", predictions)
