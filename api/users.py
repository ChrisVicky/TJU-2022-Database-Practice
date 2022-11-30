from flask import Blueprint, redirect, request, render_template, url_for
from api.service import UserService
from api.service import PostService
from utils import u_from_fu, f_from_fu, fu_in_one
from utils import log
from models import procedures
from models import db

userpage = Blueprint("userpage", __name__)

##
# @brief Get information of current user
@userpage.route("/")
def userIndex():
    fuid = request.cookies.get('fuid')
    if not fuid:
        return redirect(url_for('loginpage.login'))
    fuid = int(fuid)
    user = UserService.getUserByUid(u_from_fu(fuid), f_from_fu(fuid))
    posts = PostService.getPostsByUserId(user.fieldid, user.id)
    return render_template("user.html", user = user, posts=posts)



##
# @brief get user info (Other than you)
@userpage.route("/userinfo/<int:id>/<int:fid>")
def userInfo(id, fid):
    fuid = request.cookies.get('fuid')
    if fuid:
        fuid = int(fuid)
        uid = u_from_fu(fuid)
        if uid == int(id):
            return redirect(url_for('userpage.userIndex'))
    uid = int(id)
    fid = int(fid)
    user = UserService.getUserByUid(uid, fid)
    posts = PostService.getPostsByUserId(fid, uid)
    return render_template("otheruser.html", user=user, posts=posts)





##
# @brief user Registration
@userpage.route("/register", methods=('POST', 'GET'))
def userRegister():
    fuid = request.cookies.get('fuid')
    if fuid:
        fuid = int(fuid)
        user = UserService.getUserByUid(u_from_fu(fuid), f_from_fu(fuid))
        return render_template("user.html", user = user)
    if request.method=='POST':
        fid = request.form['fieldid']
        if fid:
            fid = int(fid)
        else:
            return render_template('500.html', msg="fid must be int")
        nickname = request.form['nickname']
        username = request.form['username']
        password = request.form['password']
        procedures.create_user(fid, nickname, username, password)
        return redirect(url_for('loginpage.login', username=username, password=password), code=307)
    return render_template('register.html')
        

##
# @brief Edit your user inform
@userpage.route("/edit", methods=('POST', 'GET'))
def userEdit():
    fuid = request.cookies.get('fuid')
    if not fuid:
        return redirect(url_for('loginpage.login'))
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    fid = f_from_fu(fuid)
    user = UserService.getUserByUid(uid, fid)
    if request.method=='POST':
        nickname = request.form['nickname']
        aboutme = request.form['aboutme']
        user.aboutme = aboutme
        user.displayname = nickname
        db.session.commit()
        return redirect(url_for('userpage.userIndex'))
    return render_template('editUser.html', user=user)
        





