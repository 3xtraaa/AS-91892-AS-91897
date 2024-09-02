from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "nancy_drew_ctlg.db"

def create_connection(db_file):
    """
    Creates a connection to the database
    :parameter    db_file - the name of the file
    :returns    connection - a connection to the database
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_home():
    return render_template("index.html")

@app.route('/all_books')
def render_all_books():
    """
    Queries the database for information about all books, store the
    information returned in a tuple. Returns the tuple to the Jinja
    template.
    """
    # Query to display all info for all books
    query = "SELECT * FROM all_nancy_drew"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE (nancy_drew_ctlg.db)
    cur.execute(query)
    all_book_info = cur.fetchall()
    con.close()
    print(all_book_info)
    return render_template('all_books.html', book_info = all_book_info)

@app.route('/not_in_library')
def render_in_library():
    """
    Queries the database for information about books which are not in the
    library, stores theinformation returned in a tuple. Returns the tuple
    to the Jinja template.
    """
    # Query to display all books in library
    query = """SELECT book_num, title, publisher
FROM all_nancy_drew
WHERE in_library is 0"""
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    not_in_library = cur.fetchall()
    con.close()
    print(not_in_library)
    return render_template('not_in_library.html', book_info = not_in_library)


if __name__ == '__main__':
  app.run()
