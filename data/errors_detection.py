import pandas as pd
df = pd.read_csv("data/clients_data_ERRORS.csv")
missing_values = df.isnull().sum()
print(missing_values)
duplicates = df[df.duplicated(subset=["PESEL"], keep=False)]
duplicates_sorted = duplicates.sort_values(by="PESEL")
print(duplicates_sorted)