# Import library
import pandas as pd

# Step 1: Load data (example CSV file)
df = pd.read_csv("data.csv")

# Step 2: Display first 5 rows
print("First 5 rows:")
print(df.head())

# Step 3: Explore data
print("\nData Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nShape of data:")
print(df.shape)

# Step 4: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Clean data
# Fill missing values with mean (for numeric columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 6: Final cleaned data
print("\nCleaned Data:")
print(df.head())
