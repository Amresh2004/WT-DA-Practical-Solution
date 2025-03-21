import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Iris dataset from CSV file
df = pd.read_csv(r'C:\Users\amresh\Downloads\iris_synthetic_data.csv')  # Ensure iris.csv is in the working directory

# Display basic statistical details (percentile, mean, std, etc.)
print("Statistical details of species (setosa, versicolor, virginica):")
print(df.groupby('species').describe())

# Features (independent variables) and target (dependent variable)
X = df.drop(columns=['species'])  # Assuming 'species' is the column name for labels
y = df['species']

# Split the dataset into training and testing sets (70:30 ratio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")