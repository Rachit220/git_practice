import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",         
        user="root",
        password="Rachit@2025",
        database="inventory_db",
        port=3306,
        connection_timeout=5
    )

    if conn.is_connected():
        print("Connected to MySQL")

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (product_name, category_id, price, quantity) VALUES (%s, %s, %s, %s)",
        ("Mouse", 1, 800, 15)
    )
    conn.commit()
    print("Product inserted")
    cursor.execute("""
        SELECT p.product_name, c.category_name, p.price, p.quantity
        FROM products p
        JOIN categories c ON p.category_id = c.category_id
    """)

    print("\n Inventory List:")
    for row in cursor.fetchall():
        print(row)

except Error as e:
    print("MySQL Error:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\n Connection closed")
