import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Create transactions dataset
dataset = [
    ['Apple', 'Mango', 'Banana'],
    ['Mango', 'Banana', 'Cabbage', 'Carrots'],
    ['Mango', 'Banana', 'Carrots'],
    ['Mango', 'Carrots']
]

# Convert dataset into DataFrame
items = sorted(set(item for transaction in dataset for item in transaction))
df = pd.DataFrame([{item: (item in transaction) for item in items} for transaction in dataset])

# Apply Apriori algorithm with different min_support values
for min_sup in [0.1, 0.2, 0.3, 0.4]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)

    print('\nAssociation Rules:')
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print(rules)
