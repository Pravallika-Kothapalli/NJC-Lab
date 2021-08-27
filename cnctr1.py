# import sqlite3
#
# mydb = sqlite3.cnctr1.connect(database="Movie")
#
# mycursor = Movie.cursor()
# mycursor.execute("select * from Movie")

import sqlite3
from sqlite3 import Error


def create_connection(Movie):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(Movie)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movie")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_Movie_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Movie WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\sqlite\db\Movie.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_Movie_by_priority(conn, 1)

        print("2. Query all Movie")
        select_all_tasks(conn)


if __name__ == '__main__':
    main()

