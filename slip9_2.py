import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Define a custom transactions dataset directly
data = {
    'TransactionID': [1, 2, 3, 4, 5, 6, 7],
    'Items': [
        'Laptop,Mouse,Keyboard',
        'Phone,Charger,Earphones',
        'Tablet,Charger,Case',
        'Laptop,Mouse,Headphones',
        'Phone,Charger,Powerbank',
        'Tablet,Keyboard,Stylus',
        'Laptop,Phone,Headphones'
    ]
}

df = pd.DataFrame(data)

# Display basic information
print("Dataset Information:")
print(df.info())

# Preprocessing: Split items into lists
df['Items'] = df['Items'].apply(lambda x: x.split(','))

# Create one-hot encoded DataFrame
items = sorted(set(item.strip() for transaction in df['Items'] for item in transaction))
encoded_df = pd.DataFrame([{item: (item.strip() in transaction) for item in items} for transaction in df['Items']])

# Apply Apriori algorithm
min_support = 0.2
frequent_itemsets = apriori(encoded_df, min_support=min_support, use_colnames=True)

print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules with a confidence threshold of 0.7
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

print("\nAssociation Rules:")
print(rules)

# Save results to a CSV file
frequent_itemsets.to_csv('custom_frequent_itemsets.csv', index=False)
rules.to_csv('custom_association_rules.csv', index=False)

print("\nResults saved to 'custom_frequent_itemsets.csv' and 'custom_association_rules.csv'")
