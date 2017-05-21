from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/User?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class User(db.Model):
     __tablename__ = 'User'
     id = db.Column(db.Integer,primary_key = True)
     username = db.Column(db.String(64),unique=True,index=True)
     password = db.Column(db.String(64))
     nickname = db.Column(db.String)
     grade = db.Column(db.Float)
     email = db.Column(db.String(80))
     wechat_name = db.Column(db.String(80))
     wechar_number = db.Column(db.String(80))
     phone = db.Column(db.String(20))
     money = db.Column(db.Float)
     address = db.Column(db.String(100))
     comment = db.Column(db.String(1000))
     level = db.Column(db.Integer)

     def __repr__(self):
         return '<User {}>'.format(self.username)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/participate')
def participate():
	return "ttt"


if __name__ == '__main__':
    app.run(debug=True)
