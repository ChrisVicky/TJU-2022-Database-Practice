from flask import Blueprint, Flask, render_template, request, url_for, redirect
from api.service import PostService
from models.semantic_embeddings import SemanticEmbeddings
from api.service import UserService
from utils import log, tag2tag
from utils import u_from_fu, f_from_fu
from models.procedures import add_tag, create_new_post
from models.posts import Posts
from models import db
from utils.ML import get_emb
from time import sleep
from models import procedures


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
@postpage.route('/<int:id>/<int:fid>')
def postIndex(id, fid):
    errorcode, post = PostService.getPost(id, fid)
    if errorcode==1:
        return render_template('500.html', msg=post)
    return render_template('post.html', post=post)

##
# @brief Create New Post
@postpage.route("/create", methods=('POST', 'GET'))
def postCreation():
    fuid = request.cookies.get('fuid')
    if fuid is None:
        return redirect(url_for('loginpage.login'))
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    fid = f_from_fu(fuid)
    user = UserService.getUserByUid(uid, fid)
    if request.method=='POST':
        fid = f_from_fu(fuid)
        title = request.form['title']
        # tags = request.form['tags']
        tags = request.form['tags']
        body = request.form['body']
        uid = u_from_fu(fuid)
        create_new_post(fid, title, tags, body, uid)
        # Show New post and Deal with Tags errorcode, post = PostService.getLastPost() if errorcode==1:
        errocode, post = PostService.getLastPost()
        sleep(2)
        if errocode:
            return render_template('500.html', msg=post)
        tags = post.tags
        tags = tag2tag(tags)
        for t in tags:
            add_tag(post.fieldid, post.id, t)
        db.session.commit()
        title_emb = get_emb([title])[0]
        input = SemanticEmbeddings(fieldid=post.fieldid, postid=post.id, embedding=title_emb)
        db.session.add(input)
        db.session.commit()
        post.user = user
        return render_template('post.html', post=post)
    return render_template('create.html')

    
##
# @brief Edit Post
@postpage.route("/edit", methods=('POST', 'GET'))
def postEdit(pid, fid):
    fuid = request.cookies.get('fuid')
    if fuid is None:
        return render_template(url_for('loginpage.login'))
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    fid = f_from_fu(fuid)
    
    post = PostService.getPost(pid, fid)
    if post is None:
        return render_template('500.html', msg="post not exist")
    if post.fieldid != fid or post.owneruserid != uid:
        return render_template('500.html', msg="Not Your Post, can't Edit it")

    if request.method=='POST':
        title = request.form['title']
        tags = request.form['tags']
        body = request.form['body']
        post.title = title
        post.tags = tags
        post.body = body

        emb = get_emb([title])[0]
        seman_entity = SemanticEmbeddings.query.filter(SemanticEmbeddings.fieldid==post.fieldid, SemanticEmbeddings.postid==post.id).one()
        if seman_entity is None:
            return render_template('500.html', msg="Semantic Not exist Error")
        seman_entity.embedding = emb

        db.session.commit()
        return redirect(url_for('postpage.postIndex', id=post.id, fid=post.fieldid))
    return render_template('editPost.html', post=post)


##
# @brief 熱榜
#
# @param id
#
# @return 
@postpage.route("/top/")
@postpage.route("/top/page/<int:id>")
def postTop(id=1):
    if id <= 0:
        id = 1
    error_code, page_num, each_page, total_page, post_list = PostService.getTopPost(id-1, pagelimit)
    if error_code:
        return render_template('500.html', msg=page_num)
    return render_template('hotposts.html', currPage=page_num, totalRecords=each_page, totalPage=total_page, posts=post_list)




@postpage.route("/comment")
def postComment():
    if request.method!='POST':
        return render_template('500.html', msg="Post Method Error")
    
    procedures.create_comment(fid, pid, uid, body)
