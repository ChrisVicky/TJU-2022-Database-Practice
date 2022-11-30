from flask import Blueprint, Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# from ..models import db
# from ..models import profanity

mainpage = Blueprint('mainpage', __name__)

##
# @brief Hello Index (Deprecated)
@mainpage.route('/')
def index():
    return render_template('hello.html')
    # all_books = books.query.all()
    # return render_template('index.html', books=all_books)

##
# @brief About me 
@mainpage.route('/about')
def aboutme():
    return render_template("about.md")

