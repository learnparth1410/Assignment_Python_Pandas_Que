
# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep='|', index_col='user_id')

# Step 4. See the first 25 entries
print("Step 4. First 25 entries:")
print(users.head(25))

# Step 5. See the last 10 entries
print("\nStep 5. Last 10 entries:")
print(users.tail(10))

# Step 6. What is the number of observations in the dataset?
num_observations = len(users)
print("\nStep 6. Number of observations in the dataset:", num_observations)

# Step 7. What is the number of columns in the dataset?
num_columns = len(users.columns)
print("\nStep 7. Number of columns in the dataset:", num_columns)

# Step 8. Print the name of all the columns
print("\nStep 8. Name of all columns:")
print(users.columns)

# Step 9. How is the dataset indexed?
print("\nStep 9. Dataset indexing:")
print(users.index)

# Step 10. What is the data type of each column?
print("\nStep 10. Data type of each column:")
print(users.dtypes)

# Step 11. Print only the occupation column
print("\nStep 11. Occupation column:")
print(users['occupation'])

# Step 12. How many different occupations are in this dataset?
num_occupations = users['occupation'].nunique()
print("\nStep 12. Number of different occupations:", num_occupations)

# Step 13. What is the most frequent occupation?
most_frequent_occupation = users['occupation'].mode()[0]
print("\nStep 13. Most frequent occupation:", most_frequent_occupation)

# Step 14. Summarize the DataFrame.
print("\nStep 14. Summary of the DataFrame:")
print(users.describe(include='all'))

# Step 15. Summarize all the columns
print("\nStep 15. Summary of all columns:")
print(users.describe(include='all'))

# Step 16. Summarize only the occupation column
print("\nStep 16. Summary of the occupation column:")
print(users['occupation'].describe())

# Step 17. What is the mean age of users?
mean_age = users['age'].mean()
print("\nStep 17. Mean age of users:", mean_age)

# Step 18. What is the age with the least occurrence?
least_occurred_age = users['age'].value_counts().idxmin()
print("\nStep 18. Age with least occurrence:", least_occurred_age)
