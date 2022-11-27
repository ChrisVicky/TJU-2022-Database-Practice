from models.users import Users
from models.user_credentials import UserCredentials
from utils import translateTime
from api.service import UserService
from sqlalchemy import String

def getUserByUid(uid:int, fid:int):
    user = Users.query.filter(Users.id==uid, Users.fieldid==fid).first()
    user.date = translateTime(user.creationdate)
    return user

def login(username:str, password:str):
    usercredentials = UserCredentials.query.filter(UserCredentials.username==username, UserCredentials.password==password).first()
    if not usercredentials:
        return 1, None
    user = UserService.getUserByUid(usercredentials.userid, usercredentials.fieldid)
    return 0, user


