from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from db import add_user, add_tutor, verify_user, verify_tutor
app = Flask(__name__)

app.config['SESSION_TYPE'] = ('filesystem')
Session(app)

# Render the home page
@app.route("/")
def home():
    if session.get('user'):
        return render_template("home.html", user = session['user'])
    else:
        return render_template("home.html")

#------------------------------------------------------------------------------------------------------
# Render how it works page
@app.route("/how-it-works")
def HIW():
    if session.get("user"):
        user = session["user"]
        return render_template("how-it-works.html", user=user)
    return render_template("how-it-works.html")

#------------------------------------------------------------------------------------------------------
# Render the find a tutor page
@app.route("/find-tutor")
def FAT():
    return render_template("find-a-tutor.html")

#------------------------------------------------------------------------------------------------------
# Render the Become A Tutor Page
@app.route("/become-tutor", methods=['GET' , 'POST'])
def BAT():
    if request.method == 'POST':
        action = request.form['action'] 
        if action == 'register':
            # Get form data for tutor registration
            email = request.form['email']
            fname = request.form['fname']
            sname = request.form['sname']
            password = request.form['password']
            # Validate form data
            if email == '' or fname == '' or sname == '' or password == '':
                return "Missing credentials"
            elif email.isspace() or fname.isspace() or sname.isspace() or password.isspace():
                return "Missing Credentials"
            # Run function in db.py to add tutor to the database
            add_tutor(fname, sname, email, password)
    return render_template("become-a-tutor.html")

#------------------------------------------------------------------------------------------------------
# Render the help page
@app.route("/help")
def help():
    return render_template("help.html")

#------------------------------------------------------------------------------------------------------
# Render the Register / Log In page
@app.route("/register-login", methods=['GET', 'POST'])
def register_login():
    error = None
    loggedIn = False

    if request.method == 'POST':
        action = request.form['action']
    
        if action == 'register':
            # Get the form data for user registration
            type = 'student'
            email = request.form['email']
            fname = request.form['fname']
            sname = request.form['sname']
            password = request.form['password']
            # Validate the data
            if email == '' or fname == '' or sname == '' or password =='':
                error = "Missing Credentials"
                return render_template("reg_log.html", error = error)
            elif email.isspace() or fname.isspace() or sname.isspace() or password.isspace():
                error = "Missing Credentials"
                return render_template("reg_log.html", error = error)
            # Run the function in db.py that will add the user information into the database
            add_user(type, fname, sname, email, password)
            return render_template("reg_log.html")

        elif action == 'login':
            email = request.form['email']
            password = request.form['password']
            if verify_user(email, password):
                user = verify_user(email, password)
                session['user']=user
                return render_template('home.html', user = session['user'])
            elif verify_tutor(email, password):
                session['email'] = email
                session['password'] = password
                return render_template('home.html', user = session['user'])
            else:
                return "Invalid credentials"
    else:
        if not session.get('user'):
            return render_template('reg_log.html')
        else:
            return render_template('home.html', user = session['user'])

#------------------------------------------------------------------------------------------------------