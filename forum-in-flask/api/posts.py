from flask import Blueprint, render_template, request, url_for, redirect
from api.service import PostService
from models.semantic_embeddings import SemanticEmbeddings
from api.service import UserService
from utils import tag2tag
from utils import u_from_fu, f_from_fu
from models.procedures import add_tag, create_new_post
from models import db
from models import procedures

try:
    from utils.ML import get_emb
except:
    from utils.ML.get_semantic import get_embedding as get_emb
from time import sleep
import re
import time
from pathlib import Path
import pickle
from utils import log

from utils.prevent_sql_injection import sql_injection_check

postpage = Blueprint('postpage', __name__)

pagelimit = 12


class PostsCache:
    def __init__(self, expire_time=3):  # 3 seconds
        self.expire_time = expire_time
        self.cache_content = None
        self.timestamp = None

    def load_cache(self, cond):
        try:
            Path("cached_posts").mkdir(parents=True, exist_ok=True)
            cache_path = f"cached_posts/{str(cond[0])}_{str(cond[1])}.pkl"
            if Path(cache_path).exists():
                with open(cache_path, "rb") as f:
                    timestamp, cache_content = pickle.load(f)
                return timestamp, cache_content
            else:
                return None, None
        except Exception:
            return None, None

    def check_expire(self, cond):
        cache_path = f"cached_posts/{str(cond[0])}_{str(cond[1])}.pkl"
        # print(f'checking expire: {cache_path}')
        if Path(cache_path).exists():
            with open(cache_path, "rb") as f:
                self.timestamp, self.cache_content = pickle.load(f)
            return int(time.time()) - self.timestamp > self.expire_time
        return True

    def cache(self, cond, body):
        """
        If the cache is expired, update the cache with the new content

        :param content: the content to be cached
        """
        if self.check_expire(cond):
            self.timestamp = int(time.time())
            self.cache_content = body

            cache_path = f"cached_posts/{str(cond[0])}_{str(cond[1])}.pkl"
            with open(cache_path, "wb") as f:
                pickle.dump((self.timestamp, self.cache_content), f)

    def get(self, offset: int = 0, limit: int = 10):
        """
        If the cache is expired, return None. Otherwise, return the cached content

        :return: the cached content
        """
        if self.check_expire((offset, limit)):
            return None
        return self.cache_content


post_cache = PostsCache(20)


##
# @brief Post Main Page
@postpage.route('/')
@postpage.route('/page/<int:id>')
def postPage(id=1):
    if id <= 0:
        id = 1

    cached = post_cache.get(id - 1, pagelimit)
    if cached is not None:
        print('post cache hit')
        error_code, page_num, each_page, total_page, post_list = cached
    else:
        error_code, page_num, each_page, total_page, post_list = PostService.getAllPost(id - 1, pagelimit)
        post_cache.cache((id - 1, pagelimit), (error_code, page_num, each_page, total_page, post_list))
    if error_code:
        return render_template('500.html', msg=page_num)
    return render_template('posts.html', currPage=page_num, totalRecords=each_page, totalPage=total_page,
                           posts=post_list)


##
# @brief Individual Post Page
@postpage.route('/<int:id>/<int:fid>')
def postIndex(id, fid):
    errorcode, post = PostService.getPost(id, fid)
    if errorcode == 1:
        return render_template('500.html', msg=post)
    fuid = request.cookies.get('fuid')
    if fuid is None:
        return render_template('post.html', post=post)
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    fid = f_from_fu(fuid)
    user = UserService.getUserByUid(uid, fid)
    return render_template('post.html', post=post, user=user)


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
    if request.method == 'POST':
        fid = f_from_fu(fuid)
        _, title = sql_injection_check(request.form['title'])
        # tags = request.form['tags']
        tags = request.form['tags']
        _, tags = sql_injection_check(tags)
        body = request.form['body']
        _, body = sql_injection_check(body)
        uid = u_from_fu(fuid)
        try:
            create_new_post(fid, title, tags, body, uid)
        except Exception as e:
            if re.search('User is banned from talking', str(e)):
                return render_template('display_exception.html',
                                       msg='You are banned from talking for 1 day! 不许说怪话😡')
            else:
                return render_template('500.html', msg=str(e))

        # Show New post and Deal with Tags errorcode, post = PostService.getLastPost() if errorcode==1:

        db.session.commit()
        errocode, post = PostService.getLastPost()
        sleep(2)
        if errocode:
            return render_template('500.html', msg=post)
        title_emb = get_emb([title])[0]
        input = SemanticEmbeddings(fieldid=post.fieldid, postid=post.id, embedding=title_emb)
        db.session.add(input)
        db.session.commit()
        post.user = user
        try:
            tags = post.tags
            tags = tag2tag(tags)
            for t in tags:
                add_tag(post.fieldid, post.id, t)
            db.session.commit()
        except Exception as e:
            pass
        return render_template('post.html', post=post, user=user)

    return render_template('create.html', user=user)


##
# @brief Edit Post
@postpage.route("/edit/<int:pid>/<int:pfid>", methods=('POST', 'GET'))
def postEdit(pid, pfid):
    fuid = request.cookies.get('fuid')
    if fuid is None:
        return render_template(url_for('loginpage.login'))
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    fid = f_from_fu(fuid)

    user = UserService.getUserByUid(uid, fid)
    errorcode, post = PostService.getPost(pid, pfid)
    if errorcode:
        return render_template("500.html", msg="Interval Error")
    if post is None:
        return render_template('500.html', msg="post not exist")
    if post.fieldid != fid or post.owneruserid != uid:
        return render_template('500.html', msg="Not Your Post, can't Edit it")

    if request.method == 'POST':
        _, title = sql_injection_check(request.form['title'])
        _, tags = sql_injection_check(request.form['tags'])
        _, body = sql_injection_check(request.form['body'])
        post.title = title
        post.tags = tags
        post.body = body

        try:
            emb = get_emb([title])[0]
            seman_entity = SemanticEmbeddings.query.filter(SemanticEmbeddings.fieldid == post.fieldid,
                                                           SemanticEmbeddings.postid == post.id).one()
            if seman_entity is None:
                return render_template('500.html', msg="Semantic Not exist Error")
            seman_entity.embedding = emb
            db.session.commit()
        except Exception as e:
            return render_template('500.html', msg="不能为空")
        return redirect(url_for('postpage.postIndex', id=post.id, fid=post.fieldid))
    return render_template('editPost.html', post=post,  user=user)


@postpage.route("/top/")
@postpage.route("/top/page/<int:id>")
def postTop(id=1):
    if id <= 0:
        id = 1
    error_code, page_num, each_page, total_page, post_list = PostService.getTopPost(id - 1, pagelimit)
    if error_code:
        return render_template('500.html', msg=page_num)
    return render_template('hotposts.html', currPage=page_num, totalRecords=each_page, totalPage=total_page,
                           posts=post_list)


@postpage.route("/comment", methods=['POST'])
def leaveComment():
    fuid = request.cookies.get('fuid')
    if fuid is None:
        return redirect(url_for('loginpage.login'))
    fuid = int(fuid)
    uid = u_from_fu(fuid)
    ufid = f_from_fu(fuid)
    user = UserService.getUserByUid(uid, ufid)
    pid = int(request.args.get('pid'))
    fid = int(request.args.get('fid'))
    log(f"{fid}: {ufid}")
    if fid != ufid:
        return render_template('500.html', msg="和你的Field不同，你不能評論")
    comment = request.form['comment']
    _, comment = sql_injection_check(comment)
    procedures.create_comment(fid, pid, user.id, comment)
    ppid = request.args.get('ppid')
    pfid = request.args.get('pfid')
    return redirect(url_for('postpage.postIndex', id=ppid, fid=pfid))
