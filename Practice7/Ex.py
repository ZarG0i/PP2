import sqlite3
import csv

DB_FILE = "phonebook.db"


def connect_db():
    return sqlite3.connect(DB_FILE)


def create_table():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            phone TEXT
        )
        """)


def insert_console():
    name = input("Enter username: ").strip()
    phone = input("Enter phone: ").strip()

    try:
        with connect_db() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (?, ?)",
                (name, phone)
            )
    except sqlite3.IntegrityError:
        print("[ERROR] Username already exists")


def insert_csv(file_path="contacts.csv"):
    try:
        with connect_db() as conn, open(file_path, "r") as f:
            cur = conn.cursor()
            reader = csv.reader(f)

            for row in reader:
                if len(row) >= 2:
                    try:
                        cur.execute(
                            "INSERT INTO phonebook (username, phone) VALUES (?, ?)",
                            (row[0], row[1])
                        )
                    except sqlite3.IntegrityError:
                        pass
    except FileNotFoundError:
        print("[ERROR] File not found")


def update_data():
    name = input("Enter username to update: ").strip()
    new_name = input("New username (optional): ").strip()
    new_phone = input("New phone (optional): ").strip()

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("""
            UPDATE phonebook
            SET username = COALESCE(?, username),
                phone = COALESCE(?, phone)
            WHERE username = ?
        """, (new_name if new_name else None,
              new_phone if new_phone else None,
              name))


def query_data():
    with connect_db() as conn:
        cur = conn.cursor()

        cur.execute("SELECT * FROM phonebook")
        for row in cur.fetchall():
            print(row)

        search = input("Search (optional): ").strip()

        if search:
            cur.execute(
                "SELECT * FROM phonebook WHERE username LIKE ?",
                (f"%{search}%",)
            )
            for row in cur.fetchall():
                print(row)


def delete_data():
    target = input("Enter username or phone to delete: ").strip()

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM phonebook WHERE username=? OR phone=?",
            (target, target)
        )


def menu():
    create_table()

    while True:
        print("\n1.Insert 2.CSV 3.Update 4.Query 5.Delete 6.Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            insert_console()
        elif choice == "2":
            insert_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break


if __name__ == "__main__":
    menu()