-- SQL

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_test_db")

cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'\
                IDENTIFIED BY 'hbnb_test_pwd'")

cursor.execute("GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost'")

cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'")

cursor.close()
conn.close()
