import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD

app = Flask("__name__")
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
=======
app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)