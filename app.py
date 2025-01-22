import pandas as pd

# Load the Excel file
df = pd.read_excel('leads.xlsx')

# Remove duplicates based on the 'name' column
df_no_duplicates = df.drop_duplicates(subset=['name'])

# Define the desired patterns to filter URLs
patterns = ['https://www.facebook.com/', 'https://linktr.ee/', 'https://instagram.com/']

# Create a mask to filter rows where the URL is missing or matches one of the patterns
mask = df_no_duplicates['url'].isna() | df_no_duplicates['url'].apply(
    lambda x: any(pattern in x for pattern in patterns) if pd.notna(x) else False
)

# Apply the mask to get the filtered DataFrame
filtered_df = df_no_duplicates[mask]

# Save the filtered DataFrame to a new Excel file
filtered_df.to_excel('filtered.xlsx', index=False)

print("Processing complete. The file 'filtered-database.xlsx' has been saved with the desired rows.")
