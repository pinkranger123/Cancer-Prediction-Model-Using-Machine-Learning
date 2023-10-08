import pandas as pd

# Option
# Data is stored in a DataFrame called 'data'
# Load your data into a pandas DataFrame
# data = pd.read_csv('path/to/your/data.csv', delimiter='\t')

# Display basic information about the data
print("Data Overview:")
print(data.info())

# Display the first few rows of the dataset to understand the structure
print("\nFirst Few Rows:")
print(data.head())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Unique values in each column to understand categorical data
print("\nUnique Values in Each Column:")
for column in data.columns:
    unique_values = data[column].unique()
    num_unique_values = len(unique_values)
    print(f"{column}: {num_unique_values} unique values")
    if num_unique_values < 20:  # Print unique values if there are fewer than 20
        print(unique_values)

# Histograms for numerical columns
data.select_dtypes(include='number').hist(figsize=(12, 10), bins=20)
plt.suptitle("Histograms for Numerical Columns")
plt.show()
