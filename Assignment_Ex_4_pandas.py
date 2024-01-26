# Step 1. Go to https://www.kaggle.com/datasets/openfoodfacts/world-food-facts/data
# Step 2. Download the dataset to your computer and unzip it.
# Assuming you have downloaded and unzipped the file to a directory.

# Step 3. Use the tsv file and assign it to a dataframe called food
import pandas as pd

# Replace 'path_to_your_file' with the actual path to the downloaded TSV file
file_path = 'D:\.vscode\assignment_python_tops/en.openfoodfacts.org.products.tsv'
food = pd.read_csv(file_path, sep='\t', low_memory=False)

# Step 4. See the first 5 entries
print("Step 4. First 5 entries:")
print(food.head())

# Step 5. What is the number of observations in the dataset?
num_observations = len(food)
print("\nStep 5. Number of observations in the dataset:", num_observations)

# Step 6. What is the number of columns in the dataset?
num_columns = len(food.columns)
print("\nStep 6. Number of columns in the dataset:", num_columns)

# Step 7. Print the name of all the columns.
print("\nStep 7. Name of all columns:")
print(food.columns)

# Step 8. What is the name of 105th column?
column_105_name = food.columns[104]  # Note: Python is zero-indexed
print("\nStep 8. Name of 105th column:", column_105_name)

# Step 9. What is the type of the observations of the 105th column?
column_105_type = food.iloc[:, 104].dtype
print("\nStep 9. Type of observations in the 105th column:", column_105_type)

# Step 10. How is the dataset indexed?
print("\nStep 10. Dataset indexing:")
print(food.index)

# Step 11. What is the product name of the 19th observation?
product_name_19th_observation = food.loc[18, 'product_name']
print("\nStep 11. Product name of the 19th observation:", product_name_19th_observation)
