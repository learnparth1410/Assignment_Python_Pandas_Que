# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
euro12 = pd.read_csv(url)

# Step 4. Select only the Goal column
goals_column = euro12['Goals']
print("Step 4. Selected Goal column:")
print(goals_column)

# Step 5. How many teams participated in the Euro2012?
num_participating_teams = euro12['Team'].nunique()
print("\nStep 5. Number of teams participated in Euro2012:", num_participating_teams)

# Step 6. What is the number of columns in the dataset?
num_columns = len(euro12.columns)
print("\nStep 6. Number of columns in the dataset:", num_columns)

# Step 7. View only the columns Team, Yellow Cards, and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nStep 7. DataFrame 'discipline':")
print(discipline)

# Step 8. Sort the teams by Red Cards, then by Yellow Cards
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print("\nStep 8. Teams sorted by Red Cards, then by Yellow Cards:")
print(discipline_sorted)

# Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow_cards = discipline['Yellow Cards'].mean()
print("\nStep 9. Mean Yellow Cards given per Team:", mean_yellow_cards)

# Step 10. Filter teams that scored more than 6 goals
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]['Team']
print("\nStep 10. Teams that scored more than 6 goals:")
print(teams_more_than_6_goals)

# Step 11. Select the teams that start with G
teams_starting_with_G = euro12[euro12['Team'].str.startswith('G')]['Team']
print("\nStep 11. Teams that start with G:")
print(teams_starting_with_G)

# Step 12. Select the first 7 columns
first_7_columns = euro12.iloc[:, :7]
print("\nStep 12. Selected first 7 columns:")
print(first_7_columns)

# Step 13. Select all columns except the last 3
all_except_last_3_columns = euro12.iloc[:, :-3]
print("\nStep 13. Selected all columns except the last 3:")
print(all_except_last_3_columns)

# Step 14. Present only the Shooting Accuracy from England, Italy, and Russia
shooting_accuracy_selected_teams = euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
print("\nStep 14. Shooting Accuracy from England, Italy, and Russia:")
print(shooting_accuracy_selected_teams)
