import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configure and Add our Database
# This tells Flask-SQLAlchemy where the database file is located
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/todo.db"

# This disables tracking modifications of objects and sending signals to the application for every database change. 
# Its a good feature but can cause memory overhead. Its should only be used where necessary.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello!'