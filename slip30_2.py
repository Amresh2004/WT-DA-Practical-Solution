import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Create the dataset
transactions = [
    ['eggs', 'milk', 'bread'],
    ['eggs', 'apple'],
    ['milk', 'bread'],
    ['apple', 'milk'],
    ['milk', 'apple', 'bread']
]

# Step 2: Convert categorical data to numeric format (One-Hot Encoding)
te = TransactionEncoder()
encoded_data = te.fit_transform(transactions)
df = pd.DataFrame(encoded_data, columns=te.columns_)

print("✅ One-Hot Encoded Data:")
print(df)

# Step 3: Apply Apriori algorithm to generate frequent itemsets
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
print("\n✅ Frequent Itemsets:")
print(frequent_itemsets)

# Step 4: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)
print("\n✅ Association Rules:")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])
