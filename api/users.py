from flask import Blueprint, redirect, request, render_template, url_for
from api.service import UserService
from utils import u_from_fu, f_from_fu, fu_in_one
from utils import log

userpage = Blueprint("userpage", __name__)

@userpage.route("/")
def userIndex():
    fuid = request.cookies.get('fuid')
    log(f"fuid {fuid}")
    if not fuid:
        return redirect(url_for('loginpage.login'))
    fuid = int(fuid)
    user = UserService.getUserByUid(u_from_fu(fuid), f_from_fu(fuid))
    return render_template("user.html", user = user)



