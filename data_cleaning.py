import pandas as pd

# Load the dataset
df = pd.read_csv('DataCleaningProject.csv.zip')

# Show first few rows
print(df.head())

# Show info about dataset
print(df.info())

# Show missing values
print(df.isnull().sum())
# Drop rows where 'director' or 'cast' are missing
df = df.dropna(subset=['director', 'cast'])

# Fill missing 'country' with 'Unknown'
df['country'] = df['country'].fillna('Unknown')
# Remove duplicates
df = df.drop_duplicates()
# Clean 'type' and 'country'
df['type'] = df['type'].str.lower().str.strip()
df['country'] = df['country'].str.title().str.strip()
# Step: Remove extra spaces from date
df['date_added'] = df['date_added'].str.strip()

# Step: Convert to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# Clean column names: lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# Remove duplicate rows if any
df = df.drop_duplicates()
# Check data types after cleaning
print(df.dtypes)
# Save to a new CSV file
df.to_csv('data_cleaned.csv', index=False)
# Expand display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)



