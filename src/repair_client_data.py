import pandas as pd

# Wczytanie danych i wyczyszczenie nazw kolumn
df = pd.read_csv("data/clients_data_ERRORS.csv")
df.columns = df.columns.str.strip().str.lower()  # Usunięcie białych znaków i zamiana na małe litery

# Sprawdzenie, czy wymagane kolumny istnieją
required_columns = {"pesel", "email", "phone"}
missing_columns = required_columns - set(df.columns)
if missing_columns:
    raise ValueError(f"BŁĄD: Brak wymaganych kolumn w pliku CSV: {missing_columns}")

# 1. Usunięcie duplikatów PESEL
duplicates_count = df.duplicated(subset=["pesel"], keep=False).sum()
df = df.drop_duplicates(subset=["pesel"], keep="first")

# 2. Sprawdzenie poprawności numeru PESEL
def validate_pesel(pesel):
    pesel = str(pesel)
    return len(pesel) == 11 and pesel.isdigit()

df["valid_pesel"] = df["pesel"].apply(validate_pesel)
invalid_pesel_records = df[~df["valid_pesel"]]

df_cleaned = df[df["valid_pesel"] & df["email"].notnull()]

# 3. Uzupełnianie brakujących e-maili na podstawie numeru telefonu
for index, row in df.iterrows():
    if pd.isnull(row["email"]):
        matching_email = df.loc[(df["phone"] == row["phone"]) & df["email"].notnull(), "email"]
        if not matching_email.empty:
            df.at[index, "email"] = matching_email.iloc[0]

# 4. Filtrowanie klientów, którym nie udało się uzupełnić e-maila
missing_email_records = df[df["email"].isnull()]

# 5. Zapisywanie poprawionych danych i problematycznych rekordów
df_cleaned= df_cleaned.drop(columns=["valid_pesel"])
df_cleaned.to_csv("data/clients_data_CLEANED.csv", index=False)
missing_email_records.to_csv("data/clients_data_MISSING.csv", index=False)
invalid_pesel_records.to_csv("data/clients_data_INVALID_PESEL.csv", index=False)

print("Poprawione dane zapisano do: data/clients_data_CLEANED.csv")
print("Klienci bez e-maila zapisani do: data/clients_data_MISSING.csv")
print("Klienci z niepoprawnym PESEL zapisani do: data/clients_data_INVALID_PESEL.csv")