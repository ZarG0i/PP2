from connect import get_connection


def search(pattern):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def add_user(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


def add_many(names, phones):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()

    cur.close()
    conn.close()


def paginate(limit, offset):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete(identifier):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (identifier,))
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    add_user("John", "12345")
    add_user("Anna", "99999")

    print("Search:")
    search("Jo")

    print("\nPagination:")
    paginate(5, 0)

    print("\nInsert many:")
    add_many(["Mike", "Bob"], ["88888", "wrong"])

    print("\nDelete:")
    delete("Anna")