# Data Cleaning Project: Filtering and Removing Duplicates from Leads Data

## Description

This project is aimed at cleaning and filtering a dataset of leads stored in an Excel file (`leads.xlsx`). The main tasks involved in the cleaning process include:
- Removing duplicate entries based on the `name` column.
- Filtering rows where URLs are either missing or match certain predefined patterns (`facebook`, `linktr.ee`, `instagram`).
- Saving the cleaned dataset into a new Excel file (`filtered.xlsx`).

## Steps

1. **Load the Data**: The dataset is read from the Excel file `leads.xlsx` using the `pandas` library.
2. **Remove Duplicates**: Duplicate rows based on the `name` column are removed.
3. **Filter URLs**: The script checks for rows where:
   - The `url` field is missing.
   - The `url` matches one of the following patterns: 
     - `https://www.facebook.com/`
     - `https://linktr.ee/`
     - `https://instagram.com/`
4. **Save Cleaned Data**: The filtered DataFrame is saved to a new Excel file called `filtered.xlsx`.

## Requirements

- Python 3.x
- `pandas` library: Install it using the following command:
  ```bash
  pip install pandas
  ```

## File Structure

- `leads.xlsx`: The original input Excel file containing the leads data.
- `filtered.xlsx`: The cleaned and filtered Excel file output after running the script.

## Usage
1. Place the `leads.xlsx` file in the project directory.
2. Run the Python script:
```bash
Copy
python clean_data.py
```
3. After execution, the cleaned data will be saved as `filtered.xlsx`.