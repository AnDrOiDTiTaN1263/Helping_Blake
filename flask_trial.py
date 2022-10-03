from flask import Flask, render_template, redirect, url_for, request
from flask import url_for
from flask import request
app = Flask(__name__)

class user:
    def __init__(self, id, username, password) :
        self.id = id
        self.username= username
        self.password = password

users =[]
users.append(user(id=1, username='admin', password='admin'))
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username =  request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()