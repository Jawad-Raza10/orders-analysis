import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")

cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Islamabad"),
    (4, "Ayesha", "Lahore"),
    (5, "Hamza", "Karachi"),
    (6, "Zain", "Peshawar")
]

orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 3000),
    (4, 2, 5800),
    (5, 3, 6200),
    (6, 3, 4000),
    (7, 4, 6000),
    (8, 5, 2500),
    (9, 6, 7000),
    (10, 5, 5500)
]

cur.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)

cur.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("Database setup completed successfully.")