import pandas as pd
import random
import faker
import sqlite3
 
fake = faker.Faker()

conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, pesel, email, phone, address, birth_date FROM customers")
existing_data = cursor.fetchall()

users = list()


def generate_pesel(birth_date):

    birth_str = birth_date.strftime('%y%m%d')
    
    unique_number = random.randint(1000, 9999)
    
    control_digit = random.randint(0, 9)
    
    pesel = birth_str + str(unique_number) + str(control_digit)
    return pesel

for _ in range(250):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}"
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")

    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
    
    pesel = generate_pesel(birth_date)
    
    users.append([first_name, last_name, pesel, email, phone, address, birth_date])
    

# Wprowadzenie błędów:
# 1. Duplikaty (losowo skopiujemy 20 wpisów z bazy danych)
duplicates = random.sample(existing_data, 20) 
users.extend(duplicates)

# 2. Brakujące wartości (losowo w 10 rekordach)
for _ in range(10):
    idx = random.randint(0, len(users) - 1)
    col_idx = random.randint(0, 6)
    users[idx][col_idx] = ""

df = pd.DataFrame(users, columns=["first_name", "last_name","pesel", "email", "phone", "addres", "birth_date"])

file_path = "data/new_users_with_errors.csv"
df.to_csv(file_path, index=False)

file_path