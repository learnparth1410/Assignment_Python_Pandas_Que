# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the given address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"
drinks = pd.read_csv(url)

# Step 4. Which continent drinks more beer on average?
continent_beer_avg = drinks.groupby('continent')['beer_servings'].mean().idxmax()
print("\nStep 4. Continent that drinks more beer on average:", continent_beer_avg)

# Step 5. For each continent, print the statistics for wine consumption.
print("\nStep 5. Statistics for wine consumption per continent:")
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print(wine_stats)

# Step 6. Print the mean alcohol consumption per continent for every column
print("\nStep 6. Mean alcohol consumption per continent:")
mean_alcohol_by_continent = drinks.groupby('continent').mean()
print(mean_alcohol_by_continent)

# Step 7. Print the median alcohol consumption per continent for every column
print("\nStep 7. Median alcohol consumption per continent:")
median_alcohol_by_continent = drinks.groupby('continent').median()
print(median_alcohol_by_continent)

# Step 8. Print the mean, min, and max values for spirit consumption. Output as a DataFrame
print("\nStep 8. Mean, min, and max values for spirit consumption:")
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max']).reset_index()
print(spirit_stats)
