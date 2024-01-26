# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# Step 4. How many products cost more than $10.00?
products_over_10_dollars = chipo[chipo['item_price'].str.replace('$', '').astype(float) > 10.00]
num_products_over_10_dollars = len(products_over_10_dollars)
print("Step 4. Number of products costing more than $10.00:", num_products_over_10_dollars)

# Step 5. What is the price of each item? Print a DataFrame with only two columns item_name and item_price
item_prices = chipo[['item_name', 'item_price']].copy()
item_prices['item_price'] = item_prices['item_price'].str.replace('$', '').astype(float)
print("\nStep 5. DataFrame with item_name and item_price:")
print(item_prices)

# Step 6. Sort by the name of the item
sorted_chipo = chipo.sort_values(by='item_name')

# Step 7. What was the quantity of the most expensive item ordered?
most_expensive_item_quantity = sorted_chipo.iloc[-1]['quantity']
print("\nStep 7. Quantity of the most expensive item ordered:", most_expensive_item_quantity)

# Step 8. How many times was a Veggie Salad Bowl ordered?
veggie_salad_bowl_orders = chipo[chipo['item_name'] == 'Veggie Salad Bowl']['quantity'].sum()
print("\nStep 8. Number of times Veggie Salad Bowl was ordered:", veggie_salad_bowl_orders)

# Step 9. How many times did someone order more than one Canned Soda?
canned_soda_multiple_orders = chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)]
num_canned_soda_multiple_orders = len(canned_soda_multiple_orders)
print("\nStep 9. Number of times someone ordered more than one Canned Soda:", num_canned_soda_multiple_orders)
