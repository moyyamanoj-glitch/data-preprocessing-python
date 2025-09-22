# data-preprocessing-python

## Objective
- Clean and prepare a raw dataset by handling nulls, duplicates, inconsistent formats.

## Steps Performed
1. Identified and handled missing values using `.isnull()` in Pandas.
2. Removed duplicate rows with `.drop_duplicates()`.
3. Standardized text values (e.g., names, gender).
4. Converted date formats to `dd-mm-yyyy`.
5. Renamed column headers (lowercase, no spaces).
6. Checked and fixed data types (age → int, date → datetime).

## Tools Used
- Python (Pandas, NumPy)
- Excel (for comparison)

## Files
- `netflix_titles.csv` → Original dataset with errors.
- `netflix_titles_cleaned.csv` → Cleaned dataset.
- `data_preprocessing.py` → code.
