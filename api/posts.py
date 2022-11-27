from flask import Blueprint, Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# from ..models import db
# from ..models import profanity
from api.service import PostService
from api.service import CommentService
from utils import log


postpage = Blueprint('postpage', __name__)

pagelimit = 12


##
# @brief Post Main Page
@postpage.route('/')
@postpage.route('/page/<int:id>')
def postPage(id=1):
    if id <= 0:
        id = 1
    error_code, page_num, each_page, total_page, post_list = PostService.getAllPost(id-1, pagelimit)
    if error_code:
        return render_template('500.html', msg=page_num)
    return render_template('posts.html', currPage=page_num, totalRecords=each_page, totalPage=total_page, posts=post_list)


##
# @brief Individual Post Page
@postpage.route('/<int:id>')
def postIndex(id):
    errorcode, post = PostService.getPost(id)
    if errorcode==1:
        return render_template('500.html', msg=post)
    log(f"comment_list: {len(post.comment_list)}")
    return render_template('post.html', post=post)



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
