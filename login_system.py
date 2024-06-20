# This code was written by chatGPT, but will need reworking inorder to work with my code
import bcrypt
import sqlite3

# Function to create the users table
def create_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT
                    )''')
    conn.commit()
    conn.close()

# Function to register a new user
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Save the username and hashed password to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password.decode('utf-8')))
    conn.commit()
    conn.close()
    print("Registration successful.")

# Function to check login credentials
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Retrieve the hashed password from the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hashed_password = result[0]
        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            print("Login successful.")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Main function
def main():
    create_table()
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

