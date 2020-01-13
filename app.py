import os
from flask import Flask, render_template, redirect, request, url_for
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


@app.route('/insert_list', methods=['POST'])
def insert_list():
    mongo.db.lists.insert_one({'list_name': request.form.get('list_name')})
    return redirect(url_for('my_lists'))


@app.route('/add_list')
def add_list():
    return render_template("add_list.html")


@app.route('/edit_list/<list_id>')
def edit_list(list_id):
    return render_template("edit_list.html",
                           list=mongo.db.lists.find_one(
                               {'_id': ObjectId(list_id)}))


@app.route('/update_list/<list_id>', methods=['POST'])
def update_list(list_id):
    mongo.db.lists.update_one(
        {'_id': ObjectId(list_id)},
        {'$set': {'list_name': request.form.get('list_name')}})
    return redirect(url_for('my_lists'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
