import os
from flask import Flask, render_template, redirect, request,\
                  url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
from flask_paginate import Pagination, get_page_parameter, get_page_args

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
@app.route('/my_page')
def my_page():
    return render_template("my_page.html",
                           title='Discover books you will love!',
                           genres=mongo.db.genres.find().sort("genre_name", 1))

# Login form
@app.route('/signin')
def signin():
    return render_template('login.html', title='Log In')

# Registration form
@app.route('/signup')
def signup():
    return render_template('register.html', title='Sign Up')

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
        flash('No account found for that username.\
        Please, try again or Sign Up.', 'error')
        return redirect(url_for('signin'))

# Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one(
            {'username': request.form['username']})

        if existing_user is None:
            users.insert_one({'username': request.form['username'],
                              'book_list': [{'id': 'Books I Liked',
                                             'value': []}]})
            session['username'] = request.form['username']
            flash('You were successfully registered and logged in.', 'success')
            return redirect(url_for('my_page'))

        flash('That username already exists! Try again or Sign In', 'error')
        return redirect(url_for('signup'))

# Log out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!', 'success')
    return redirect(url_for('my_page'))

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

    username = session.get("username")

    return render_template("get_books.html", title='Search Results',
                           user=mongo.db.users.find_one(
                               {'username': username}),
                           search_results=search_results,
                           search_word=search_word,
                           pagination=pagination, total=total)

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

    username = session.get("username")

    return render_template("books_by_genre.html", title='Search Results',
                           genre=mongo.db.genres.find_one(
                               {'_id': ObjectId(genre_id)}),
                           user=mongo.db.users.find_one(
                               {'username': username}),
                           pagination=pagination,
                           total=total, books=books)

# Display user lists
@app.route('/my_lists')
def my_lists():
    if session.get("username"):
        username = session.get("username")
        return render_template("my_lists.html", title='My Lists',
                               user=mongo.db.users.find_one(
                                   {'username': username}),
                               book=mongo.db.books.find())

# Insert new list
@app.route('/insert_list', methods=['POST'])
def insert_list():
    if session.get("username"):
        username = session.get("username")
        user = mongo.db.users.find_one({'username': username})

        list_name = request.form.get('list_name')

        existingList = []
        for obj in user["book_list"]:
            existingList.append(obj["id"])

        if list_name not in existingList:
            mongo.db.users.update_one({"username": username},
                                      {'$push':
                                      {'book_list':
                                       {'id': list_name,
                                        'value': []}}})
            flash('New list successfully created', 'success')
            return redirect(url_for('my_lists'))
        else:
            flash("This list name is already exists! Try again.",
                  'error')
            return redirect(url_for('add_list'))
    return redirect(url_for('my_page'))

# Add new list form
@app.route('/add_list')
def add_list():
    return render_template("add_list.html", title='Add List')

# Edit list form
@app.route('/edit_list/<list_id>')
def edit_list(list_id):
    if session.get("username"):
        username = session.get("username")
        user = mongo.db.users.find_one({'username': username},
                                       {'book_list.id': list_id})
        return render_template("edit_list.html", title='Edit List',
                               user=user, list_id=list_id)

# Send updated list to MongoDB
@app.route('/update_list/<list_id>', methods=['POST'])
def update_list(list_id):
    if session.get("username"):
        username = session.get("username")
        mongo.db.users.update_one(
            {'username': username,
             'book_list.id': list_id},
            {'$set': {'book_list.$.id': request.form.get('list_name')}})
        return redirect(url_for('my_lists'))

# Delete list from database
@app.route('/delete_list/<list_id>')
def delete_list(list_id):
    if session.get("username"):
        username = session.get("username")
        mongo.db.users.update_one({'username': username,
                                   'book_list.id': list_id},
                                  {'$pull': {'book_list': {'id': list_id}}})
        return redirect(url_for('my_lists'))

# Insert book into list in MongoDB
@app.route('/insert_book_into_list/<list_id>/<book_id>', methods=['POST'])
def insert_book_into_list(list_id, book_id):
    if session.get("username"):
        username = session.get("username")
        user = mongo.db.users.find_one({'username': username})

        list_name = request.form.get('list_name')

        for obj in user['book_list']:
            if obj["id"] == list_name:
                if book_id not in obj['value']:
                    mongo.db.users.update_one(
                        {'username': username,
                            'book_list.id':  list_name},
                        {'$push': {'book_list.$.value': book_id}})
                else:
                    flash("This book is already in a list!", 'error')
                    return redirect(url_for('my_page'))
                return redirect(url_for('show_list',
                                        list_id=list_name))

# Show books in a list
@app.route('/show_list/<list_id>')
def show_list(list_id):
    if session.get("username"):
        username = session.get("username")
        user = mongo.db.users.find_one({'username': username})
        books = []
        for obj in user["book_list"]:
            if obj["id"] == list_id:
                for item in obj["value"]:
                    book = mongo.db.books.find_one({"_id": ObjectId(item)})
                    books.append(book)

        # Pagination
        def get_books(offset=0, per_page=4):
            return books[offset: offset + per_page]

        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')
        per_page = 4
        offset = (page - 1) * per_page

        total = len(books)
        pagination_books = get_books(offset=offset, per_page=per_page)

        pagination = Pagination(page=page, per_page=per_page,
                                total=total, offset=offset,
                                bs_version=4,
                                css_framework='foundation',
                                record_name='results')

        return render_template("show_list.html", user=user,
                               pagination=pagination,
                               page=page, per_page=per_page,
                               offset=offset,
                               list_id=list_id, results=pagination_books,
                               total=total)

# Delete book from list in database
@app.route('/delete_book/<list_id>/<book_id>')
def delete_book(list_id, book_id):
    if session.get("username"):
        username = session.get("username")
        mongo.db.users.update_one({'username': username,
                                   'book_list.id': list_id},
                                  {'$pull': {'book_list.$.value': book_id}})
        return redirect(url_for('show_list', list_id=list_id))

# @app.route('/insert_book', methods=['POST'])
# def insert_book():
#     books = mongo.db.books
#     books.insert_one(request.form.to_dict())
#     return redirect(url_for('add_book'))


# @app.route('/add_book')
# def add_book():
#     return render_template("add_book.html", title='Add Book',
#                            genres=mongo.db.genres.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
