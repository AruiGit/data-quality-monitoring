import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie poprawionych danych
df = pd.read_csv("data/clients_data_CLEANED.csv")
df.to_excel("reports/clean_customers.xlsx")

# Liczenie duplikatów pesel przed usunięciem (sprawdzamy na oryginalnym zbiorze)
original_df = pd.read_csv("data/clients_data_ERRORS.csv")
duplicates_count = original_df.duplicated(subset=["pesel"], keep=False).sum()
original_df[original_df.duplicated(subset=["pesel"], keep=False)] \
    .sort_values(by="pesel") \
    .to_excel("reports/duplicated_pesels.xlsx", index=False)

# Liczenie braków w e-mailach
missing_email_df = pd.read_csv("data/clients_data_MISSING.csv")
missing_email_count = len(missing_email_df)
missing_email_df.to_excel("reports/missing_emails.xlsx")

# Liczenie niepoprawnych pesel
invalid_pesel_df = pd.read_csv("data/clients_data_INVALID_PESEL.csv")
invalid_pesel_count = len(invalid_pesel_df)
invalid_pesel_df.to_excel("reports/invalid_pesels.xlsx")

# Obliczenie liczby poprawnych rekordów
total_records = len(original_df)
correct_records = total_records - (duplicates_count + missing_email_count + invalid_pesel_count)

# Generowanie raportu tekstowego
report = f"""
=== RAPORT POPRAWY JAKOŚCI DANYCH ===
Łączna liczba rekordów: {total_records}
Liczba poprawnych rekordów: {correct_records}
Liczba duplikatów pesel przed usunięciem: {duplicates_count}
Liczba rekordów z brakującym e-mailem: {missing_email_count}
Liczba niepoprawnych pesel-i: {invalid_pesel_count}

Pliki wynikowe:
✔ data/clients_data_CLEANED.csv - poprawione dane
✔ data/clients_data_missing.csv - klienci bez uzupełnionego e-maila
✔ data/clients_data_invalid_pesel.csv - klienci z niepoprawnym pesel-em
"""

print(report)

# Zapis raportu do pliku tekstowego
with open("reports/quality_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("Raport został zapisany do: reports/quality_report.txt")

# Tworzenie wykresu
labels = ["Poprawne dane", "Duplikaty pesel", "Braki e-mail", "Niepoprawne pesel"]
values = [correct_records, duplicates_count, missing_email_count, invalid_pesel_count]
colors = ["green", "red", "orange", "purple"]

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=colors)
plt.xlabel("Typ błędu")
plt.ylabel("Liczba rekordów")
plt.title("Jakość danych klientów")
plt.xticks(rotation=20)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Zapisanie wykresu do pliku
plt.savefig("reports/data_quality_chart.png")
plt.show()

print("Wykres zapisano jako: reports/data_quality_chart.png")