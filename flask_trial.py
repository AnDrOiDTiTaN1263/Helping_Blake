from crypt import methods
from fileinput import filename
from click import password_option


from flask import Flask, render_template
from flask import url_for
from flask import request
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('index.html')
@app.route('/', methods=['GET' 'POST'])
def check_creds():
    if request.method=='GET':
        return f"The URL /data is accessed directly. Try going to '/form'"
    if request.method == 'POST':
        form_data = request.form
        return render_template('questions.html', form_data = form_data)
if __name__ == "__main__":
    app.run()