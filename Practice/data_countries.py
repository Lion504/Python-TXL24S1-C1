import pandas as pd

file_path = r'C:\Program Files\MariaDB 11.5\data\country\countries.csv'

# Reading the CSV with specific parameters and handling bad lines
df = pd.read_csv(file_path, delimiter=',', quotechar='"', on_bad_lines='skip')

# Show all columns in the DataFrame
pd.set_option('display.max_columns', None)

# Display the first 10 rows again
print(df[df.isna().any(axis=1)])




