##
# @file CommentService.py
# @brief 
# @author Christopher Liu
# @version 1.0
# @date 2022-11-24

from models.comments import Comments
from models.users import Users
from utils import translateTime, log

def getCommentByPostId(id, fieldid):
    comments_list = Comments.query.filter(Comments.fieldid==fieldid, Comments.postid==id).all()
    for c in comments_list:
        c.displayname = Users.query.filter(Users.id==c.userid, Users.fieldid==fieldid).first().displayname
        c.date = translateTime(c.creationdate)
    return comments_list


