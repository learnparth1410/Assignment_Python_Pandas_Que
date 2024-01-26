# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
users = pd.read_csv(url, sep='|', index_col='user_id')

# Step 4. Discover what is the mean age per occupation
mean_age_per_occupation = users.groupby('occupation')['age'].mean()
print("\nStep 4. Mean age per occupation:")
print(mean_age_per_occupation)

# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
def male_ratio(series):
    male_count = (series == 'M').sum()
    total_count = series.count()
    return male_count / total_count

male_ratio_per_occupation = users.groupby('occupation')['gender'].agg(male_ratio).sort_values(ascending=False)
print("\nStep 5. Male ratio per occupation (sorted):")
print(male_ratio_per_occupation)

# Step 6. For each occupation, calculate the minimum and maximum ages
age_range_per_occupation = users.groupby('occupation')['age'].agg(['min', 'max'])
print("\nStep 6. Minimum and maximum ages per occupation:")
print(age_range_per_occupation)

# Step 7. For each combination of occupation and gender, calculate the mean age
mean_age_by_occupation_gender = users.groupby(['occupation', 'gender'])['age'].mean()
print("\nStep 7. Mean age for each combination of occupation and gender:")
print(mean_age_by_occupation_gender)

# Step 8. For each occupation, present the percentage of women and men
gender_percentage_per_occupation = users.groupby(['occupation', 'gender']).size() / users.groupby('occupation').size()
print("\nStep 8. Percentage of women and men per occupation:")
print(gender_percentage_per_occupation)
