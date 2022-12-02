##
# @file CommentService.py
# @brief Comments 
# @author Christopher Liu
# @version 1.0
# @date 2022-11-24

from models.comments import Comments
from models.users import Users
from utils import translateTime, log

##
# @brief Get Comments by post id AND fieldid
#
# @param id
# @param fieldid
#
# @return 
def getCommentByPostId(id, fieldid):
    comments_list = Comments.query.filter(Comments.fieldid==fieldid, Comments.postid==id).all()
    for c in comments_list:
        us = Users.query.filter(Users.id==c.userid, Users.fieldid==fieldid).first()
        if us is None:
            c.displayname = None
        else:
            c.displayname = us.displayname
        c.date = translateTime(c.creationdate)
    return comments_list


