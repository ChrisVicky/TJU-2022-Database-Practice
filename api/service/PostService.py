##
# @file PostService.py
# @brief Post Service 
# @author Christopher
# @version 1.0
# @date 2022-11-24

from models.comments import Comments
from models.posts import Posts
from models.users import Users
from api.service import CommentService
from utils import translateTime, log


##
# @brief get All Post -- With Paging, ordered by creationdate , desc
#
# @param offset:int --> Page offset + 1
# @param limit:int  --> Limit posts in each Page
#
# @return offset+1 (offset start with ZERO) , limit, post_list
def getAllPost(offset:int=0, limit:int=10):
    try:
        post_list = Posts.query.filter(Posts.parentid==None).order_by(Posts.creationdate.desc()).limit(limit).offset(offset*limit).all()
        total_post = Posts.query.count()
        total_page = int(total_post / limit)
        for p in post_list:
            p.author = Users.query.filter(Users.id==p.owneruserid, Users.fieldid==p.fieldid).first().displayname
            p.date = translateTime(p.creationdate)
            p.answercount = Posts.query.filter(Posts.parentid==p.id, Posts.fieldid==p.fieldid).count()
            p.commentcount = Comments.query.filter(Comments.postid==p.id, Comments.fieldid==p.fieldid).count()
        return 0, offset+1, limit, total_page, post_list
    except Exception as e:
        return 1, e, None, None, None



##
# @brief get post with id
#
# @param id destination ID
#
# @return post --> author = displayname,  creationdate is set as format in translateTime
def getPost(id):
    try:
        post = Posts.query.filter_by(id=id).first()
        author = Users.query.filter_by(id=post.owneruserid).first()
        post.author = author.displayname
        post.date = translateTime(post.creationdate)
        # 获取评论
        post.comment_list = CommentService.getCommentByPostId(id, post.fieldid)
        post.answers = getPostByParentId(id, post.fieldid)
        post.commentcount = len(post.comment_list)
    except Exception as e:
        return 1, e
    return 0, post


def getPostByParentId(id, fieldid):
    post_list = Posts.query.filter(Posts.parentid==id,Posts.fieldid==fieldid).all()
    for p in post_list:
        p.author = Users.query.filter_by(id=p.owneruserid)[0].displayname
        p.date = translateTime(p.creationdate)
        p.comment_list = CommentService.getCommentByPostId(p.id, p.fieldid)
        p.commentcount = len(p.comment_list)
        log(f"Found Comments: {len(p.comment_list)}")
        p.answers = getPostByParentId(p.id, p.fieldid)
        p.answercount = len(p.answers)
        log(f"Fount Answers: {len(p.answers)}")
    return post_list
