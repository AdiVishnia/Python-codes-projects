import sqlite3

# Connect to your database (note the file name!)
conn = sqlite3.connect(r"C:\Users\Home\Desktop\BLACKBOX7\game_database.db")
cursor = conn.cursor()

# Adding a new user
username = "adi"
password = "123456"

cursor.execute("""
INSERT INTO users (username, password)
VALUES (?, ?)
""", (username, password))

# Saving the changes
conn.commit()

print("User created successfully with ID:", cursor.lastrowid)

# Check - retrieving all users from the table
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Closing the connection
conn.close()