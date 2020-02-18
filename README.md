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


## Features

#### Existing Features


#### Features Left To Implement
* add confirm box on deletion of the list

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


## Deployment

* Deployment to Heroku

Install Flask:  
$ pip install flask
 
Install Flask-PyMongo  
$ pip install Flask-PyMongo  
$ pip install dnspython

Install Flask Paginate
$ easy_install -U flask-paginate
or alternatively if you have pip installed:
$ pip install -U flask-paginate



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
* User registration/sign in
  * https://www.youtube.com/watch?v=vVx1737auSE&list=PL7OAaGksQ4dDPXn7iDR_ezFSmUYcObbpj&index=18&t=0s
  * https://github.com/MiroslavSvec/DCD_lead

#### Images
Logo image created with the help of [www.looka.com](https://looka.com/)
Background images: [register.html](https://wallpapersafari.com/w/E5tL3S), [login.html](https://torontostoreys.com/real-estate-terms/), [background](https://all-free-download.com/free-photos/download/paper-texture-image-5_169361.html) 
Cover page images of the books are from [www.amazon.co.uk](https://www.amazon.co.uk/)

#### Acknowledgement
* Video tutorials of Code Institute and examples of introduced code;
* Flask [Documentation](https://flask.palletsprojects.com/en/1.1.x/) 
* Flask Paginate [Documentation](https://pythonhosted.org/Flask-paginate/)
* MongoDB [Documentation](https://docs.mongodb.com/)
* Especially I want to thank my mentor Nishant and tutor Michael for all the support I got through the project.