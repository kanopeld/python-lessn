from datetime import date

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

class User:
    firstname = ''
    lastname = ''
    age = 0

    def __init__(self, form):
        self.firstname = form['firstname']
        self.lastname = form['lastname']
        self.age = form['age']


@app.route('/form', methods=['POST'])
def form():
    user = User(request.form)
    print(user)
    return 'Success'


if __name__ == '__main__':
    # print(app.url_map)
    app.run(port=8000)
