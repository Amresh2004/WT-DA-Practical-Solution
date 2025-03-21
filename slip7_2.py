import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Create Market Basket dataset
data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'Items': [
        'Bread,Milk',
        'Bread,Diaper,Beer,Eggs',
        'Milk,Diaper,Beer,Coke',
        'Bread,Milk,Diaper,Beer',
        'Bread,Milk,Diaper,Coke'
    ]
}

df = pd.DataFrame(data)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Preprocessing: Split items into columns
df['Items'] = df['Items'].apply(lambda x: x.split(','))

# Convert items into a one-hot encoded DataFrame
items = sorted(set(item for sublist in df['Items'] for item in sublist))
encoded_df = pd.DataFrame([{item: (item in transaction) for item in items} for transaction in df['Items']])

# Apply Apriori algorithm with a minimum support of 0.2
min_support = 0.2
frequent_itemsets = apriori(encoded_df, min_support=min_support, use_colnames=True)

print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules with a confidence threshold of 0.7
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

print("\nAssociation Rules:")
print(rules)

# Save results to a CSV file
frequent_itemsets.to_csv('frequent_itemsets.csv', index=False)
rules.to_csv('association_rules.csv', index=False)

print("\nResults saved to 'frequent_itemsets.csv' and 'association_rules.csv'")
