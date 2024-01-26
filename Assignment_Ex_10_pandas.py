# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Create the DataFrame with the given values
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks',
                         'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons',
                         'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st',
                        '2nd', '2nd', '1st', '1st', '2nd', '2nd'],
            'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze',
                     'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger',
                     'Riani', 'Ali'],
            'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3,
                             2, 3],
            'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57,
                              62, 70, 62, 70]}

# Step 3. Assign it to a variable called regiment
regiment = pd.DataFrame(raw_data)

# Step 4. What is the mean preTestScore from the regiment Nighthawks?
mean_pretest_nighthawks = regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()
print("\nStep 4. Mean preTestScore from the regiment Nighthawks:", mean_pretest_nighthawks)

# Step 5. Present general statistics by company
company_statistics = regiment.groupby('company').describe()
print("\nStep 5. General statistics by company:")
print(company_statistics)

# Step 6. What is the mean of each company's preTestScore?
mean_pretest_by_company = regiment.groupby('company')['preTestScore'].mean()
print("\nStep 6. Mean preTestScore of each company:")
print(mean_pretest_by_company)

# Step 7. Present the mean preTestScores grouped by regiment and company
mean_pretest_by_regiment_company = regiment.groupby(['regiment', 'company'])['preTestScore'].mean()
print("\nStep 7. Mean preTestScores grouped by regiment and company:")
print(mean_pretest_by_regiment_company)

# Step 8. Present the mean preTestScores grouped by regiment and company without hierarchical indexing
mean_pretest_flat_index = regiment.groupby(['regiment', 'company'], as_index=False)['preTestScore'].mean()
print("\nStep 8. Mean preTestScores grouped by regiment and company without hierarchical indexing:")
print(mean_pretest_flat_index)

# Step 9. Group the entire dataframe by regiment and company
grouped_data = regiment.groupby(['regiment', 'company'])

# Step 10. What is the number of observations in each regiment and company
observations_count = grouped_data.size()
print("\nStep 10. Number of observations in each regiment and company:")
print(observations_count)

# Step 11. Iterate over a group and print the name and the whole data from the regiment
print("\nStep 11. Iterate over a group and print the name and the whole data from the regiment:")
for name, group_data in grouped_data:
    print("\nGroup Name:", name)
    print(group_data)
