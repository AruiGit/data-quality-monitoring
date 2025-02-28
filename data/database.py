import sqlite3
import pandas as pd

# Połączenie z bazą
conn = sqlite3.connect("clients.db")
cursor = conn.cursor()

# Wczytanie danych z CSV
df = pd.read_csv("data/clients_data.csv")

# Wstawienie danych do tabeli
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO customers (first_name, last_name, pesel, email, phone, address, birth_date) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row["Imię"], row["Nazwisko"], row["PESEL"], row["Email"], row["Telefon"], row["Adres"], row["DataUrodzenia"]))

# Zapisanie zmian
conn.commit()
conn.close()

print("Dane załadowane do bazy SQLite!")