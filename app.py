import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/my_page')
def my_page():
    return render_template("my_page.html", books=mongo.db.books.find())


@app.route('/my_lists')
def my_lists():
    return render_template("my_lists.html", lists=mongo.db.lists.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
