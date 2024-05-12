from flask import Flask, render_template, request, redirect, url_for, flash
from connector import login_datos

app = Flask(__name__)
app.secret_key = b'\xc6\xdfo\xcf\xe6S\xb4\xa0\xdf\xb8z\xb6\xb4^Q]'

db = login_datos()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_result = db.busca_users(username)
        password_result = db.busca_password(password)

        if user_result and password_result:
            if user_result[0][1] == username and password_result[0][2] == password:
                return redirect(url_for('dashboard'))
        flash('Usuario o contraseña incorrectos')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Bienvenido al Dashboard'

if __name__ == '__main__':
    app.run(debug=True)
