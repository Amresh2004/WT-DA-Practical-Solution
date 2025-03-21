import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Create new dataset
car_data = [
    ['Tata', 'Nexon', '2017'],
    ['MG', 'Astor', '2021'],
    ['KIA', 'Seltos', '2019'],
    ['Hyundai', 'Creta', '2015']
]

# Convert dataset into DataFrame
car_df = pd.DataFrame(car_data, columns=['company', 'model', 'year'])

# Convert categorical data into numeric using one-hot encoding
car_df_encoded = pd.get_dummies(car_df)

# Apply Apriori algorithm with different min_support values
for min_sup in [0.1, 0.2, 0.3, 0.4]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(car_df_encoded, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)

    print('\nAssociation Rules:')
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print(rules)
