
# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep='\t')

# Step 4. See the first 10 entries
print("Step 4. First 10 entries:")
print(chipo.head(10))

# Step 5. What is the number of observations in the dataset?
num_observations = len(chipo)
print("\nStep 5. Number of observations in the dataset:", num_observations)

# Step 6. What is the number of columns in the dataset?
num_columns = len(chipo.columns)
print("\nStep 6. Number of columns in the dataset:", num_columns)

# Step 7. Print the name of all the columns
print("\nStep 7. Name of all columns:")
print(chipo.columns)

# Step 8. How is the dataset indexed?
print("\nStep 8. Dataset indexing:")
print(chipo.index)

# Step 9. Which was the most-ordered item?
most_ordered_item = chipo['item_name'].value_counts().idxmax()
print("\nStep 9. Most-ordered item:", most_ordered_item)

# Step 10. For the most-ordered item, how many items were ordered?
items_ordered = chipo[chipo['item_name'] == most_ordered_item]['quantity'].sum()
print("\nStep 10. Number of items ordered for the most-ordered item:", items_ordered)

# Step 11. What was the most ordered item in the choice_description column?
most_ordered_choice = chipo['choice_description'].value_counts().idxmax()
print("\nStep 11. Most-ordered item in choice_description column:", most_ordered_choice)

# Step 12. How many items were ordered in total?
total_items_ordered = chipo['quantity'].sum()
print("\nStep 12. Total items ordered:", total_items_ordered)

# Step 13. Turn the item price into a float
# Step 13.a. Check the item price type
print("\nStep 13.a. Item price type before conversion:")
print(chipo['item_price'].dtype)

# Step 13.b. Create a lambda function and change the type of item price
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))  # Removing '$' and converting to float

# Step 13.c. Check the item price type
print("\nStep 13.c. Item price type after conversion:")
print(chipo['item_price'].dtype)

# Step 14. How much was the revenue for the period in the dataset?
revenue = (chipo['quantity'] * chipo['item_price']).sum()
print("\nStep 14. Revenue for the period:", revenue)

# Step 15. How many orders were made in the period?
num_orders = chipo['order_id'].nunique()
print("\nStep 15. Number of orders made in the period:", num_orders)

# Step 16. What is the average revenue amount per order?
average_revenue_per_order = revenue / num_orders
print("\nStep 16. Average revenue amount per order:", average_revenue_per_order)

# Step 17. How many different items are sold?
num_different_items = chipo['item_name'].nunique()
print("\nStep 17. Number of different items sold:", num_different_items)
