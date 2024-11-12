from flask import Flask, render_template, request, redirect, url_for, session
from db import add_user, add_tutor, verify_user
app = Flask(__name__)
app.secret_key = 'hello123'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/how-it-works")
def HIW():
    return render_template("how-it-works.html")

@app.route("/find-tutor")
def FAT():
    return render_template("find-a-tutor.html")

@app.route("/become-tutor", methods=['GET' , 'POST'])
def BAT():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'register':
            email = request.form['email']
            fname = request.form['fname']
            sname = request.form['sname']
            password = request.form['password']
    return render_template("become-a-tutor.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/register-login", methods=['GET', 'POST'])
def register_login():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'register':
            email = request.form['email']
            fname = request.form['fname']
            sname = request.form['sname']
            password = request.form['password']
            if email == '' or fname == '' or sname == '' or password =='':
                return "Missing credentials"
            add_user(fname, sname, email, password)
            return render_template("reg_log.html")
        elif action == 'login':
            email = request.form['email']
            password = request.form['password']
            if verify_user(email, password):
                session['email'] = email
                return redirect(url_for('/home'))
            else:
                return "Invalid credentials"
    return render_template("reg_log.html")

