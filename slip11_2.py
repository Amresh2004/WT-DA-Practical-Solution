import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Define the new dataset directly
data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'Items': [
        'butter,bread,milk',
        'butter,flour,milk,sugar',
        'butter,eggs,milk,salt',
        'eggs',
        'butter,flour,milk,salt'
    ]
}

# Convert dataset into DataFrame
df = pd.DataFrame(data)

# Display basic information
print("Dataset Information:")
print(df.info())

# Preprocessing: Split items into lists
df['Items'] = df['Items'].apply(lambda x: x.split(','))

# One-hot encode items
items = sorted(set(item.strip() for transaction in df['Items'] for item in transaction))
encoded_df = pd.DataFrame([{item: (item.strip() in transaction) for item in items} for transaction in df['Items']])

# Apply Apriori algorithm with different min_support values
for min_support in [0.2, 0.3, 0.4]:
    print(f"\nResults for min_support = {min_support}")
    
    # Generate frequent itemsets
    frequent_itemsets = apriori(encoded_df, min_support=min_support, use_colnames=True)
    print("\nFrequent Itemsets:")
    print(frequent_itemsets)

    # Generate association rules with a confidence threshold of 0.7
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print("\nAssociation Rules:")
    print(rules)

    # Save results to CSV files
    frequent_itemsets.to_csv(f'itemsets_min_sup_{min_support}.csv', index=False)
    rules.to_csv(f'rules_min_sup_{min_support}.csv', index=False)

print("\nResults saved for all min_support values!")