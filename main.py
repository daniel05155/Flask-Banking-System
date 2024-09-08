import re
import MySQLdb.cursors
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6d7g8h9i10'  # Secret key

# --Database connection details -- #w
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10051005'   # Replace ******* with  your database password.
app.config['MYSQL_DB'] = 'BankingSystem'

# Intialize MySQL
mysql = MySQL(app)

# --Login -- #
@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    # POST Method && Form is not NULL
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:    
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        
        # Fetch one record and return result
        account_info = cursor.fetchone()
        
        # Check if account exists using MySQL
        if account_info:
            session['loggedin'] = True
            session['id']       = account_info['id']
            session['username'] = account_info['username']
            return redirect(url_for('home'))  # Redirect to home page
        else:
            flash("Incorrect username/password!", "danger")
            
    return render_template('auth/login.html', title="Online Banking System")  

# --Register -- #
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # POST Method && Form is not NULL
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # --Account Validation -- #
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        ## If account exists show error and validation checks
        # cursor.execute('SELECT * FROM accounts WHERE username = %s', username)  ## Error
        cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )   
        account = cursor.fetchone()
        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Incorrect username/password!", "danger")
        
        # Account doesnt exists and the form data is valid, now insert new account into accounts table    
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))
            # return  render_template('home/home.html', username=session['username'], title="Home")   # return redirect(url_for('login'))
    
    # Form is empty... (No POST Data)
    if request.method == 'POST':
        flash("Please fill out the form!", "danger")
        return render_template('auth/register.html', title="Register")

    # GET Request
    return render_template('auth/register.html', title="Register")

# Home Page
@app.route('/')
def home():
    # User is loggedin show them the home page
    if 'loggedin' in session:
        return render_template('home/home.html', username=session['username'], title="Home")
    
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))    

@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        return render_template('auth/profile.html', 
                                username=session['username'],
                                title="User Profile")
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))  

if __name__ =='__main__':
	app.run(debug=True)  
