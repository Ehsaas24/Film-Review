from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)


@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)


