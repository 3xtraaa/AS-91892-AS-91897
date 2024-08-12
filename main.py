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

@app.route('/in_library')
def render_in_library():
    # Query to display all books in library
    query = "SELECT "

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
