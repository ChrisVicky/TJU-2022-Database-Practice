##
# @file PostService.py
# @brief Post Service 
# @author Christopher
# @version 1.0
# @date 2022-11-24

from models.comments import Comments
from models.posts import Posts
from models.tags import Tags
from models.users import Users
from api.service import CommentService
from utils import translateTime, log
from api.service import TagService
from models.top import Top
from models import db


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
def getPost(id, fid):
    try:
        post = Posts.query.filter(Posts.id==id, Posts.fieldid==fid).first()
        author = Users.query.filter(Users.id==post.owneruserid, Users.fieldid==post.fieldid).first()
        post.author = author.displayname
        post.date = translateTime(post.creationdate)
        # 获取评论
        post.comment_list = CommentService.getCommentByPostId(id, post.fieldid)
        log("answers got")
        post.answers = getPostByParentId(id, post.fieldid)
        if post.answercount is None:
            post.answercount = 0
        post.commentcount = len(post.comment_list)
        post.tags_list = TagService.getPostTags(post.fieldid, id)
        post.user = author
    except Exception as e:
        return 1, e
    return 0, post


##
# @brief ..
#
# @param id
# @param fieldid
#
# @return 
def getPostByParentId(id, fieldid):
    post_list = Posts.query.filter(Posts.parentid==id,Posts.fieldid==fieldid).all()
    for p in post_list:
        try:
            p.author = Users.query.filter_by(id=p.owneruserid)[0].displayname
        except:
            p.author = None
        p.date = translateTime(p.creationdate)
        p.comment_list = CommentService.getCommentByPostId(p.id, p.fieldid)
        p.commentcount = len(p.comment_list)
    return post_list


##
# @brief get post with id
#
# @param id destination ID
#
# @return post --> author = displayname,  creationdate is set as format in translateTime
def getPostByFidPid(fid:int, pid:int, score):
    post = Posts.query.filter(Posts.fieldid==fid, Posts.id==pid).one()
    author = Users.query.filter(Users.id==post.owneruserid, Users.fieldid==post.fieldid).first()
    if author is None:
        post.author = post.owneruserid
    else:
        post.author = author.displayname
    post.date = translateTime(post.creationdate)
    post.score = int(score * 100)
    if post.answercount is None:
        post.answercount = 0
    return post


##
# @brief Get Posts by Search results
#
# @param search_res:list [(fid, pid, emb-score), ...]
#
# @return 
def getPostsBySearch(search_res:list):
    posts = []
    for r in search_res:
        posts.append(getPostByFidPid(r[0], r[1], r[2])) 
    return posts


##
# @brief Get the Latest Post --> When Post been Created
#
# @return 
def getLastPost():
    try:
        post = Posts.query.order_by(Posts.creationdate.desc()).first()
        author = Users.query.filter_by(id=post.owneruserid).first()
        post.author = author.displayname
        post.date = translateTime(post.creationdate)
        # 获取评论
        post.comment_list = CommentService.getCommentByPostId(post.id, post.fieldid)
        post.answers = getPostByParentId(post.id, post.fieldid)
        post.commentcount = len(post.comment_list)
        if post.answercount == None:
            post.answercount = 0
        post.tags_list = TagService.getPostTags(post.fieldid, post.id)
    except Exception as e:
        return 1, e
    return 0, post


def getPostsByUserId(fid, uid):
    posts = Posts.query.filter(Posts.fieldid==fid, Posts.owneruserid==uid).all()
    for p in posts:
        p.author = Users.query.filter(Users.id==p.owneruserid, Users.fieldid==p.fieldid).first().displayname
        p.date = translateTime(p.creationdate)
        if p.answercount == None:
            p.answercount = 0
        # p.answercount = Posts.query.filter(Posts.parentid==p.id, Posts.fieldid==p.fieldid).count()
        # p.commentcount = Comments.query.filter(Comments.postid==p.id, Comments.fieldid==p.fieldid).count()
    return posts


def getTopPost(offset:int=0, limit:int=10):
    try:
        post_list = Top.query.filter(Top.parentid==None).order_by(Top.creationdate.desc()).limit(limit).offset(offset*limit).all()
        total_post = Top.query.count()
        total_page = int(total_post / limit)

        db.session.close()
        for p in post_list:
            p.author = Users.query.filter(Users.id==p.owneruserid, Users.fieldid==p.fieldid).first().displayname
            p.date = translateTime(p.creationdate)
            # p.answercount = Posts.query.filter(Posts.parentid==p.id, Posts.fieldid==p.fieldid).count()
            # p.commentcount = Comments.query.filter(Comments.postid==p.id, Comments.fieldid==p.fieldid).count()
        return 0, offset+1, limit, total_page, post_list
    except Exception as e:
        return 1, e, None, None, None


