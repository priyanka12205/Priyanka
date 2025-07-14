import pandas as pd

# Set the path to your CSV file
file_path = r"C:\Users\yarla\OneDrive\Desktop\Student PY\Student_performance_data.csv"

# Load the data
df = pd.read_csv(file_path)

# Display basic information
print("📊 Dataset Info:")
print(df.info())

# Show first 5 rows
print("\n🔍 First 5 Rows:")
print(df.head())

# Check for missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Basic statistics
print("\n📈 Descriptive Statistics:")
print(df.describe(include='all'))

# Unique values per column
print("\n🔢 Unique values in each column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Example: Group by gender and average score
if 'gender' in df.columns and 'math score' in df.columns:
    print("\n📚 Average Math Score by Gender:")
    print(df.groupby('gender')['math score'].mean())
