import sqlite3
import pandas as pd

# Połączenie z bazą
conn = sqlite3.connect("clients.db")
cursor = conn.cursor()

# Wyczyszczenie bazy
cursor.execute("DELETE FROM customers")

# Wczytanie danych z CSV
df = pd.read_csv("data/clients_data_CLEANED.csv")

# Wstawienie danych do tabeli
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO customers (first_name, last_name, pesel, email, phone, address, birth_date) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (row["first_name"], row["last_name"], row["pesel"], row["email"], row["phone"], row["addres"], row["birth_date"]))

# Zapisanie zmian
conn.commit()
conn.close()

print("Dane załadowane do bazy SQLite!")