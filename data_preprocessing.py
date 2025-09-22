import pandas as pd

# Load dataset
df = pd.read_csv(r"c:/Users/Manoj Kumar/Downloads/netflix_titles.csv")

# Handle missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# fill NaNs in text columns with "unknown" and "--"
df['director'] = df['director'].fillna("unknown")
df['cast'] = df['cast'].fillna("--")
df['country'] = df['country'].fillna("unknown")
df['rating'] = df['rating'].fillna("unknown")
df['duration'] = df['duration'].fillna("--")
df['date_added'] = df['date_added'].fillna("01-01-1900") 


# Remove duplicate rows
df = df.drop_duplicates()

# Standardize text values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

# Convert date formats
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Rename column headers
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fix data types
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype("Int64")

print("\nMissing values after cleaning:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)
print("\nPreview:\n", df.head())

# Save cleaned file
df.to_csv("c:/Users/Manoj Kumar/Downloads/netflix_titles_cleaned.csv", index=False)
print("\n✅ Cleaned file saved as 'netflix_titles_cleaned.csv'")


