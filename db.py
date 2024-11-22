import sqlite3
from flask import g, Flask, render_template, request, redirect, url_for, session
from users import user
app = Flask(__name__)

if __name__ =="__main__":
    app.run(debug=True)

# THis is checking the connection to the database
def get_db_connection():
    conn = sqlite3.connect('GMJ.db', timeout=10)
    return conn

# Connects the program to the database. Enables the program to execute modifications to the database, in this case, adding a user.
def add_user(type, fname, sname, email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (type ,FirstName, Surname, Email, Password) VALUES (?, ?, ?, ?, ?)", (type, fname, sname, email, password))
    conn.commit()

    id = cursor.lastrowid
    return user(id, type, fname, sname, email, password)

# Verifies the details that were entered when logging in
def verify_user(email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    return user

def add_tutor(fname, sname, email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tutors (FirstName, Surname, Email, Password) VALUES (?, ?, ?, ?)", (fname, sname, email, password))
    conn.commit()

def verify_tutor(email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tutors WHERE Email = ? AND password = ?", (email, password))
    tutor = cursor.fetchone()
    return tutor