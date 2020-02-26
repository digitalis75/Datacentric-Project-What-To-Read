# Data Centric Project - What To Read

 What To Read (or WTR) is an application that allows user to search the book catalog for books 
that they would like to read. The search can be done by word (full text search) and by genre 
by clicking buttons with name of genre.
 Also logged-in users can save books in provided default list or in lists they've created themselves.

## UX
This application can be very useful for people who love books. It can help them with organising books 
that they are planning to read and for keeping a track of the books they read.

Users can check out for more information about a book and/or purchase it from www.amazon.co.uk website 
by clicking on a button provided for each book.

#### User story

As a user I would like to be able to:
* easily navigate the website and find what I want;
* easily search for books and find books in the same category;
* find more information about the book;
* understand how to register and login;
* save a book in a list;
* delete a book from the list;
* create a new list, edit its name or delete it;
* view my lists and books in each list;

## Wireframes
Wireframes are created in Balsamiq Cloud.

Wireframes for desktop:
 * [my_page.html](wireframes/desktop/my_page_html.jpg)
 * [register.html](wireframes/desktop/register_html.jpg)
 * [login.html](wireframes/desktop/login_html.jpg)
 * [get_books.html](wireframes/desktop/get_books_html.jpg)
 * [books_by_genre.html](wireframes/desktop/books_by_genre_html.jpg)
 * [my_lists.html](wireframes/desktop/my_lists_html.jpg)
 * [add_list.html](wireframes/desktop/add_list_html.jpg)
 * [edit_list.html](wireframes/desktop/edit_list_html.jpg)
 * [show_list.html](wireframes/desktop/show_list_html.jpg)
 * [add_book.html](wireframes/desktop/add_book_html.jpg)

Wireframes for mobile devices:
 * [my_page.html](wireframes/mobile/mob_my_page.jpg)
 * [register.html](wireframes/mobile/mob_register.jpg)
 * [login.html](wireframes/mobile/mob_login.jpg)
 * [get_books.html](wireframes/mobile/mob_get_books.jpg)
 * [books_by_genre.html](wireframes/mobile/mob_books_by_genre.jpg)
 * [my_lists.html](wireframes/mobile/mob_my_lists.jpg)
 * [add_list.html](wireframes/mobile/mob_add_list.jpg)
 * [edit_list.html](wireframes/mobile/mob_edit_list.jpg)
 * [show_list.html](wireframes/mobile/mob_show_list.jpg)

## Features

#### Existing Features
* Login/registration
  * User sign in - allows user to sign in and create book lists and save books.
  * User sign up - allows user to register.
  * User sign out - sign out user.
* Lists
  * Create list - allows to registered user to create a book list.
  * Edit list - allows to registered user to edit name of the list.
  * Delete list - allows to registered user to delete a list.
* Books
  * Search for books using full text search - allows search for a book by title, by author and by word.
  * Search for books by genre - allows search for a book by genre.
  * Add book to list - allows to registered user to add a book to the list.
  * View books in a list - allows to registered user to view added to a list books.
  * Delete book - allows to registered user to delete a book from a list.
  * View book info on www.amazon.co.uk - brings user to amazon.co.uk to the books page.
* Admin area
  * Insert books into database - only for administrator, allows to insert a book into MongoDB
* Flash messaging - allowing to see how successful was certain action.
* Pagination - allows to show search results in pages.

#### Features Left To Implement
* add confirm box on deletion of the list
* contact us and social media links
* highlight active links in pagination 

## Technology Used
* HTML5
* CSS3
* JQuery
* Python (a programming language used to create the backend)
* Flask (a microframework for Python)
* MongoDB (a NoSQL Database which uses documents to store data)
* MongoDB Atlas (global cloud database service for modern applications)
* GitHub
* gitpod

## Testing
The HTML code was checked with online validator:(https://validator.w3.org/#validate_by_input);  
The CSS code was checked with online validator: (https://jigsaw.w3.org/css-validator/#validate_by_input);
The Chrome Developer Tools was used to check website for responsiveness;

I carried out manual tests to check that all features work as expected. These tests are documented in user_testing.pdf and can
be viewed [here](tests/user_testing.pdf).  

I have also tested my project for responsiveness and on different browsers which is detailed in browser_tests.pdf and can be viewed [here](tests/browser_tests.pdf).

## Deployment

There are two branches, one is for production and one for development. For development environ variables are set from a file.  For Heroku the environ variables are set in Config Vars in Heroku settings.
Project was developed in gitpod, and used git and GitHub for version control.

### Heroku

This project is deployed on Heroku hosting platform.  
View 'What To Read' [here](https://what-to-read-app.herokuapp.com/).

To deploy this project I needed to:
* sign up to Heroku (Heroku.com) and create Heroku app
* include a Procfile - tells Heroku what type of app it is and what to run  
  $ echo web: python app.py > Procfile
* include a requirements.txt - tells Heroku what dependencies to install  
  $ pip3 freeze -- local > requirements.txt
* in Heroku Settings set the Config Vars for the IP, PORT, MONGO_URI and unique secret key.
* configure dynos in Heroku.
* in Heroku Deploy section connect to project GitHub repository and enable automatic deploy from master branch.


### Local

To run project locally:  
* clone the repository:  
  $ git clone https://github.com/digitalis75/Datacentric-Project-What-To-Read.git

* install the dependencies in requirements.txt:  
  $ pip install -r requirements.txt
  
  or 

  Install Flask:  
  $ pip install flask
 
  Install Flask-PyMongo  
  $ pip install Flask-PyMongo  
  $ pip install dnspython

  Install Flask Paginate  
  $ easy_install -U flask-paginate  
  or alternatively if you have pip installed:  
  $ pip install -U flask-paginate

* create database in MongoDB and set the following environment variables:  
  MONGO_URI=[Database URI]  
  MONGO_DBNAME=[Database Name]  
  SECRET=[Some key combination]  
* Run the project  
  $ python3 app.py

## Credit
#### Content
* [Google fonts](https://fonts.google.com/?category=Serif&query=roboto);  
* [Font Awesome](https://fontawesome.com/);
* [Materialize(0.100.2)](http://archives.materializecss.com/0.100.2/about.html)

#### Code
* Pagination
  * https://pythonhosted.org/Flask-paginate/,
  * https://harishvc.com/2015/04/15/pagination-flask-mongodb/,
  * https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9,
  * https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo
* Text search
  * https://www.mongodb.com/blog/post/integrating-mongodb-text-search-with-a-python-app
* Flash method
  * https://www.youtube.com/watch?v=lcVdZtVvnnk
* Modal
  * https://stackoverflow.com/questions/40937631/modals-created-in-jinja-conditional-statement-are-all-showing-the-same-data
* User registration/login
  * https://www.youtube.com/watch?v=vVx1737auSE&list=PL7OAaGksQ4dDPXn7iDR_ezFSmUYcObbpj&index=18&t=0s
  * https://github.com/MiroslavSvec/DCD_lead

#### Images
Logo image created with the help of [www.looka.com](https://looka.com/)  
Background images: [register.html](https://wallpapersafari.com/w/E5tL3S), [login.html](https://torontostoreys.com/real-estate-terms/), [background](https://all-free-download.com/free-photos/download/paper-texture-image-5_169361.html)   
Cover page images of the books are from [www.amazon.co.uk](https://www.amazon.co.uk/)

#### Acknowledgement
* Video tutorials of Code Institute and examples of introduced code;
* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/) 
* [Flask Paginate Documentation](https://pythonhosted.org/Flask-paginate/)
* [MongoDB Documentation](https://docs.mongodb.com/)