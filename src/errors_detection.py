import pandas as pd

def validate_pesel(pesel):
    return len(str(pesel)) == 11 and str(pesel).isdigit()

df = pd.read_csv("data/clients_data_ERRORS.csv")
missing_values = df.isnull().sum()
print("Brakujące wartości w kolumnach: ")
print(missing_values)

duplicates = df[df.duplicated(subset=["pesel"], keep=False)]
duplicates_sorted = duplicates.sort_values(by="pesel")
print("\nDupliakty peseli:" )
print(duplicates_sorted)

df["valid_pesel"] = df["pesel"].astype(str).apply(validate_pesel)
invalid_pesel = df[~df["valid_pesel"]] 
print("\nNiepoprawne numery pesel:")
print(invalid_pesel)