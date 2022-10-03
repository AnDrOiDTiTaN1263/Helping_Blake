
from flask import Flask, render_template, redirect, url_for, request
from flask import url_for
from flask import request
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials for administrative account'
        else:
            return redirect(url_for('questions'))
    return render_template('login.html', error= error)
if __name__ == "__main__":
    app.run()