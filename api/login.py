from flask import Blueprint, Flask, make_response, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
# from ..models import db
# from ..models import profanity
from api.service import PostService
from api.service import CommentService
from api.service import UserService
from utils import fu_in_one
from models.users import Users
from utils import log
loginpage = Blueprint('loginpage', __name__)

@loginpage.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, user = UserService.login(username, password)
        if success:
            # Login Failed
            return render_template("500.html", msg="Login Error")
        log(f"Login Success: {user.id}")
        ckstring = str(fu_in_one(user.fieldid, user.id))
        log(f"ckstring: {ckstring}")
        res = make_response(redirect(url_for('userpage.userIndex')))
        res.set_cookie('fuid', ckstring)
        return res

    # TODO: Logout, without Log out interface, a customer won't be able to change accounts
    # fuid = request.cookies.get('fuid')
    # log(f"fuid {fuid}")
    # if not fuid:
    #     return render_template('login.html')
    # return redirect(url_for('userpage.userIndex'))
    return render_template("login.html")


