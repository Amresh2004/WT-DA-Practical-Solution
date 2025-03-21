import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample data for User dataset
data = {
        'User ID': [1, 2, 3, 4, 5],
        'Gender': ['Male', 'Female', 
        'Male', 'Female', 'Male'],
        'Age': [25, 30, 35, 40, 45], 
        'EstimatedSalary': [50000, 60000, 70000, 80000, 90000], 
        'Purchased': [0, 1, 0, 1, 0]
}

# Create DataFrame
user_df = pd.DataFrame(data)

# Preprocessing: Encode Gender and split features and target
le = LabelEncoder()
user_df['Gender'] = le.fit_transform(user_df['Gender'])

# Features and target
X = user_df.drop(columns=['Purchased', 'User ID'])  # Dropping 'User ID' as it is not needed for prediction
y = user_df['Purchased']

# Split data and scale features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and evaluate logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# Output the accuracy and classification report
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))