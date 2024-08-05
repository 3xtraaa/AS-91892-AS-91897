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

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
