CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    pesel VARCHAR(11),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    created_at DATE
);