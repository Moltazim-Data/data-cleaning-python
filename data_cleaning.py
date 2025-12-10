import pandas as pd
from pathlib import Path

# Paths
data_dir = Path("data")
input_file = data_dir / "customer_data.csv"
output_file = data_dir / "customer_data_cleaned.csv"

print(f"Loading data from: {input_file}")

# Load data
df = pd.read_csv(input_file)

print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Info:")
print(df.info())

print("\n🔹 Missing values per column:")
print(df.isna().sum())

print("\n🔹 Number of duplicated rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\n✅ Duplicates removed.")
print(f"New shape: {df.shape}")

# Standardize column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print("\n🔹 New column names:")
print(df.columns)

# Simple missing value handling
num_cols = df.select_dtypes(include="number").columns
cat_cols = df.select_dtypes(exclude="number").columns

print("\n🔹 Numeric columns:", list(num_cols))
print("🔹 Categorical columns:", list(cat_cols))

for col in num_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

for col in cat_cols:
    mode_value = df[col].mode()[0]
    df[col] = df[col].fillna(mode_value)

print("\n✅ Missing values filled.")
print(df.isna().sum())

# Save cleaned data
df.to_csv(output_file, index=False)
print(f"\n💾 Cleaned dataset saved to: {output_file}")

print("\n🎉 Data cleaning script finished successfully.")

