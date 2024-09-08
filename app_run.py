import re
from flask import Flask,  request, render_template, redirect,  url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6d7g8h9i1011j'

# Intialize MySQL
mysql = MySQL(app)

# --Database connection details -- #
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '10051005'   # Replace ******* with  your database password.
app.config['MYSQL_DB'] = 'loginapp'

# --Login -- #
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account_info = cursor.fetchone()
        if account_info:
            session['loggedin'] = True
            session['id']       = account_info['id']
            session['username'] = account_info['username']
            return  render_template('home/home.html', username=session['username'], title="Home")
        else:
            return flash('Incorrect username/password!')
    else:
        return render_template('auth/login.html', title="Login")

# --Register -- #
@app.route('/login/register', methods=['GET', 'POST'])
def register():
    # POST Method && Form is not NULL
    if request.method=='POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email    = request.form['email']
        
        # --Account Validation -- #
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', [username])
        account_check = cursor.fetchone()       
        print(account_check)

        # Repeated items 
        if account_check!=None:
            return flash('Account already exists!')
        # --Account Info is under rule or not -- #
        elif not re.match(r'[A-Za-z0-9]+', username):
            return flash('Username must contain only characters and numbers!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not username or not password or not email:
            flash("username/password/email is not blank!", "danger") 

        # Insert new account without problem
        else:
            cursor.execute("INSERT INTO accounts(username, email, password) VALUES(%s, %s, %s)",(username, email, password))
            mysql.connection.commit()
            flash('Contratulations! You Have Successfully Registered!')
            return redirect(url_for('login'))
    
    #  POST Method && Form is NULL || GET Method
    elif request.method=='POST':
        flash('Please Fill Out the Form!')
    
    else:
        return render_template('auth/register.html', title="Register")

@app.route('/', methods=["GET","POST"])
def home():

    return redirect(url_for('login')) 
   
if __name__ == '__main__':
    app.run(debug=True, port=3000)