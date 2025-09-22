# data-preprocessing-python

## Objective
- Clean and prepare a raw dataset by handling nulls, duplicates, inconsistent formats.

## Steps Performed
1. Identified and handled missing values using `.isnull()` in Pandas.
2. Removed duplicate rows with `.drop_duplicates()`.
3. Standardized text values.
4. Converted date formats to `dd-mm-yyyy`.
5. Renamed column headers.
6. Checked and fixed data types.

## Tools Used
- Python (Pandas, NumPy)
- Excel (for comparison)

## Files
- `netflix_titles.csv` → Original dataset with errors.
- `netflix_titles_cleaned.csv` → Cleaned dataset.
- `data_preprocessing.py` → code.
