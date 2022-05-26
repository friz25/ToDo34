from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Columb(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Bolean)

db.create_all() #создали нашу БД

@app.get("/")
def home():
    return "Hello, Wolrd MOTHERFUCKER!"