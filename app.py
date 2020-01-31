import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
from flask_paginate import Pagination, get_page_parameter

if path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

app.config["MONGO_DBNAME"] = 'what_to_read'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

mongo.db.books.create_index(
    [
        ("title", "text"),
        ("author", "text"),
        ("genre_name", "text"),
        ("image_url", "text"),
        ("amazon", "text")
    ])


@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html', title='Log In')


@app.route('/my_page')
def my_page():
    return render_template("my_page.html",
                           title='Discover books you will love!',
                           genres=mongo.db.genres.find().sort("genre_name", 1))

# User login
@app.route('/login', methods=['POST'])
def login():
    login_user = mongo.db.users.find_one({'username': request.form['username']})
    # Log in existing user
    if login_user:
        session['username'] = request.form['username']
        flash('Welcome back! You are logged in.', 'success')
        return redirect(url_for('my_page'))
    else:
        flash('No account found for that email address.\
        Please, Try again or Sign Up.', 'error')
        return render_template('login.html', title='Sign In')

# Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one(
            {'username': request.form['username']})

        if existing_user is None:
            users.insert({'username': request.form['username']})
            session['username'] = request.form['username']
            return redirect(url_for('my_page'))

        flash('That username already exists! Try again or Sign In', 'error')
        return render_template('register.html', title='Sign Up')

# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!', 'success')
    return redirect(url_for('index'))

# Show search results by word
@app.route('/search_results', methods=['GET'])
def search_results():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    per_page = 4
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # Search by word
    search_word = request.args.get("search_word")
    search_results = mongo.db.books.find(
                {"$text":
                    {"$search": search_word}}).sort('_id', 1)\
                                              .skip((page-1)*per_page)\
                                              .limit(per_page)
    # Total of search results
    total = search_results.count()
    # Pagination
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, search=search,
                            search_results=search_results,
                            bs_version=4,
                            css_framework='foundation',
                            record_name='results')

    return render_template("get_books.html", title='Search Results',
                           lists=list(mongo.db.lists.find()),
                           search_results=search_results,
                           search_word=search_word,
                           pagination=pagination,
                           total=total)

# Show search results by genre
@app.route('/books_by_genre/<genre_id>', methods=['GET', 'POST'])
def books_by_genre(genre_id):
    per_page = 4
    page = request.args.get(get_page_parameter(), type=int, default=1)
    genre = mongo.db.genres.find_one(
                               {'_id': ObjectId(genre_id)})
    books = mongo.db.books.find({'genre_name': genre["genre_name"]})\
        .sort('_id', 1)\
        .skip((page-1)*per_page)\
        .limit(per_page)

    # Total of search results
    total = books.count()
    # Pagination
    pagination = Pagination(page=page, per_page=per_page,
                            total=total,
                            books=books,
                            bs_version=4,
                            css_framework='foundation',
                            record_name='results')
    return render_template("books_by_genre.html", title='Search Results',
                           genre=mongo.db.genres.find_one(
                               {'_id': ObjectId(genre_id)}),
                           lists=list(mongo.db.lists.find()),
                           pagination=pagination,
                           total=total, books=books)

# Display lists
@app.route('/my_lists')
def my_lists():
    return render_template("my_lists.html", title='My Lists',
                           lists=mongo.db.lists.find())

# Insert new list
@app.route('/insert_list', methods=['POST'])
def insert_list():
    mongo.db.lists.insert_one({'list_name': request.form.get('list_name')})
    return redirect(url_for('my_lists'))

# Add new list form
@app.route('/add_list')
def add_list():
    return render_template("add_list.html", title='Add List')

# Edit list form
@app.route('/edit_list/<list_id>')
def edit_list(list_id):
    return render_template("edit_list.html", title='Edit List',
                           list=mongo.db.lists.find_one(
                               {'_id': ObjectId(list_id)}))

# Send updated list to MongoDB
@app.route('/update_list/<list_id>', methods=['POST'])
def update_list(list_id):
    mongo.db.lists.update_one(
        {'_id': ObjectId(list_id)},
        {'$set': {'list_name': request.form.get('list_name')}})
    return redirect(url_for('my_lists'))

# Delete list from database
@app.route('/delete_list/<list_id>')
def delete_list(list_id):
    mongo.db.lists.delete_one({'_id': ObjectId(list_id)})
    return redirect(url_for('my_lists'))


@app.route('/showlist/<list_id>')
def showlist(list_id):
    return render_template("show_list.html",
                           list=mongo.db.lists.find_one(
                               {'_id': ObjectId(list_id)}))


@app.route('/insert_book', methods=['POST'])
def insert_book():
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('add_book'))


@app.route('/add_book')
def add_book():
    return render_template("add_book.html", title='Add Book',
                           genres=mongo.db.genres.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
