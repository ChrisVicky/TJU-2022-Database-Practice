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
from utils.prevent_sql_injection import sql_injection_check
loginpage = Blueprint('loginpage', __name__)

##
# @brief Login 
@loginpage.route('/', methods=('GET', 'POST'))
def login():
    fuid = request.cookies.get('fuid')
    if fuid:
        return redirect(url_for('userpage.userIndex'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, user = UserService.login(username, password)
        if success:
            # Login Failed
            # return render_template("500.html", msg="Login Error")
            return render_template("display_exception.html", msg="登录有误，请检查用户名和密码")
        log(f"Login Success: {user.id}")
        ckstring = str(fu_in_one(user.fieldid, user.id))
        _, ckstring = sql_injection_check(ckstring)
        log(f"ckstring: {ckstring}")
        res = make_response(redirect(url_for('userpage.userIndex')))
        res.set_cookie('fuid', ckstring)
        return res

    return render_template("login.html")

##
# @brief Logout
@loginpage.route('/logout')
def logout():
    fuid = request.cookies.get('fuid')
    if not fuid:
        return redirect(url_for('loginpage.login'))
    res = make_response(redirect(url_for('loginpage.login')))
    res.delete_cookie('fuid')
    return res


