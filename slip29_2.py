import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
data = {
    'Student_ID': range(1, 21),
    'Score': [45, 63, 33, 85, 50, 70, 90, 20, 77, 82, 48, 59, 72, 38, 92, 35, 62, 74, 40, 89],
    'Pass': [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1]  # 1 = Pass, 0 = Fail
}

df = pd.DataFrame(data)

print(df.head())
X = df[['Score']]  # Independent variable (Score)
y = df['Pass']      # Dependent variable (Pass/Fail)

# Split data into training and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Display confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display precision, recall, f1-score
print("Classification Report:")
print(classification_report(y_test, y_pred))
# Plot sigmoid curve
plt.scatter(df['Score'], df['Pass'], color='blue', label='Actual Data')
plt.plot(X_test, model.predict_proba(X_test)[:,1], color='red', label='Logistic Regression Curve')
plt.axhline(0.5, color='gray', linestyle='--', label='Decision Boundary')
plt.xlabel('Score')
plt.ylabel('Probability of Passing')
plt.legend()
plt.show()
