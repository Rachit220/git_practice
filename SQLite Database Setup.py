print("LINE 1")

import mysql.connector

print("LINE 2")

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Rachit@2025",
    port=3306,
    connection_timeout=5
)

print("LINE 3")
conn.close()
print("LINE 4")

