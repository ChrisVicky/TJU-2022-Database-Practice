from flask import Blueprint, Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from models import db
from models import profanity

app = Blueprint('api', __name__)

@app.route('/')
def index():
    return render_template('hello.html')
    # all_books = books.query.all()
    # return render_template('index.html', books=all_books)

# @app.route('/<int:id>/')
# def getBook(id):
#     book = books.query.get_or_404(id)
#     return render_template('book.html', book=book)
#
#
# @app.route("/create/", methods=('GET', 'POST'))
# def create():
#     if request.method=='POST':
#         title = request.form['title']
#         author = request.form['author']
#         review = request.form['review']
#         page = request.form['page']
#         book = books(title=title,
#                      author=author,
#                      review=review,
#                      pages_num=page,
#                     )
#         db.session.add(book)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('create.html')
#
#
# @app.route('/<int:id>/edit/', methods=('GET', 'POST'))
# def editReview(id):
#     book = books.query.get_or_404(id)
#
#     if request.method=='POST':
#         title = request.form['title']
#         author = request.form['author']
#         review = request.form['review']
#         page = request.form['page']
#
#         book.title = title
#         book.author = author
#         book.review = review
#         book.page = page
#
#         db.session.add(book)
#         db.session.commit()
#
#         return redirect(url_for('index'))
#     return render_template('edit.html', book=book)
#
#
#
# @app.route('/<int:id>/delete/')
# def deleteReview(id):
#     book = books.query.get_or_404(id)
#     db.session.delete(book)
#     db.session.commit()
#     return redirect(url_for('index'))
#
#
#
#
#
