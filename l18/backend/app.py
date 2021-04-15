from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///flask.sqlite'

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Main page', age=16, users=[{'name': 'Ilya'}, {'name': 'Vania'}])


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    age = db.Column(db.Integer)
    email = db.Column(db.String(255))

    def __init__(self, form):
        self.firstname = form['firstname']
        self.lastname = form['lastname']
        self.age = form['age']
        self.email = form['email']


@app.route('/user/create', methods=['POST'])
def form():
    user = User(request.form)
    db.session.add(user)
    db.session.commit()

    return 'success!'


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(port=8000)
