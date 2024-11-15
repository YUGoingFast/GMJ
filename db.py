import sqlite3
from flask import g, Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

if __name__ =="__main__":
    app.run(debug=True)

def get_db_connection():
    conn = sqlite3.connect('GMJ.db', timeout=10)
    return conn

def add_user(fname, sname, email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (FirstName, Surname, Email, Password) VALUES (?, ?, ?, ?)", (fname, sname, email, password))
    conn.commit()
    conn.close()

def verify_user(email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE Email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_tutor(fname, sname, email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tutors (FirstName, Surname, Email, Password) VALUES (?, ?, ?, ?)", (fname, sname, email, password))
    conn.commit()
    conn.close()

def verify_tutor(email, password):
    conn = sqlite3.connect('GMJ.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tutors WHERE Email = ? AND password = ?", (email, password))
    tutor = cursor.fetchone()
    conn.close()
    return tutor is not None