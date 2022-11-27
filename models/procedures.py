from sqlalchemy import String
from . import exec_pro
from posts import Posts
from users import Users
from utils import getCurrentTimeStamp

SE = "StackExchange"
CM = "Common"

##
# "StackExchange"."add_tag"
#   ("field_id" int4, "post_id" int4, "tag" text)
#
# @brief Add tag (Perhaps Deprecated)
#
# @param field_id:int
# @param post_id:int
# @param tag:String
#
# @return 
def add_tag(field_id:int, post_id:int, tag:String):
    params = (field_id, post_id, tag)
    exec_pro(SE, "add_tag", params)

##
# "StackExchange"."alter_post"
#     ("in_field_id" int4, "in_post_id" int4, "in_title" text, "in_tags" text, "in_body" text, "in_author_id" int4, "in_date" int4)
#
# @brief Alter Post Interface
#
# @param old_post:Posts -- old post
# @param title          -- new title
# @param tags           -- new tags 
# @param body           -- new body
# @param user:Users     -- who perform the alter
#
# @return 
def alter_post(old_post:Posts, title:String, tags:String, body:String, user:Users):
    date = getCurrentTimeStamp()
    params = (user.fieldid, old_post.id, title, tags, body, user.id, date)
    exec_pro(SE, "alter_post", params)
    
##
#"StackExchange"."answer_post"
#   ("in_field_id" int4, "in_post_id" int4, "in_body" text, "in_author_id" int4, "in_date" int4)
#
# @brief Post to answer another post
#
# @param field_id:int
# @param parent_post_id:int
# @param body:String
# @param user_id:int
#
# @return NONE
def answer_post(field_id:int, parent_post_id:int, body:String, user_id:int):
    date = getCurrentTimeStamp()
    params = (field_id, parent_post_id, body, user_id, date)
    exec_pro(SE, "answer_post", params)

##
#"StackExchange"."create_comment"
#   ("in_field_id" int4, "in_post_id" int4, "in_user_id" int4, "in_comment_text" text, "in_comment_date" int4)
# @brief 
#
# @param fid:int        -- field id
# @param pid:int        -- post id
# @param uid:int        -- user id
# @param body:String    -- comment
#
# @return None
def create_comment(fid:int, pid:int, uid:int, body:String):
    date = getCurrentTimeStamp()
    params = (fid, pid, uid, body, date)
    exec_pro(SE, "create_comment", params)

## 
# "StackExchange"."create_new_post"
#   ("in_field_id" int4, "in_title" text, "in_tags" text, "in_body" text, "in_author_id" int4, "in_date" int4)
#
# @brief Create New Post
#
# @param fid:int
# @param title:String
# @param tags:String
# @param body:String
# @param uid:int
#
# @return 
def create_new_post(fid:int, title:String, tags:String, body:String, uid:int):
    date = getCurrentTimeStamp()
    params = (fid, title, tags, body, uid, date)
    exec_pro(SE, "create_new_post", params)


## 
# "StackExchange"."create_user"
#   ("in_field_id" int4, "in_creation_date" int4, "in_display_name" text, "in_username" text, "in_password" text)
# 
# @brief 
#
# @param fid:int
# @param nickname:String
# @param username:String
# @param password:String
#
# @return 
def create_user(fid:int, nickname:String, username:String, password:String):
    date = getCurrentTimeStamp()
    params = (fid, date, nickname, username, password)
    exec_pro(SE, "create_user", params)


## 
# "StackExchange"."delete_comment"
# ("in_field_id" int4, "in_comment_id" int4)
# 
# @brief 
#
# @param fid:int
# @param cid:int
#
# @return 
def delete_comment(fid:int, cid:int):
    params = (fid, cid)
    exec_pro(SE, "delete_comment", params)

##
# "StackExchange"."delete_downvote"
#   ("post_id" int4, "field_id" int4)
# 
# @brief 
#
# @param pid:int
# @param fid:int
#
# @return 
def delete_downvote(pid:int, fid:int):
    params = (pid, fid)
    exec_pro(SE, "delete_downvote", params)

##
# "StackExchange"."delete_post"
#   ("in_field_id" int4, "in_post_id" int4)
# 
# @brief 
#
# @param fid:int
# @param pid:int
#
# @return 
def delete_post(fid:int, pid:int):
    params = (fid, pid)
    exec_pro(SE, "delete_post", params)

##
# "StackExchange"."delete_upvote"
#   ("post_id" int4, "field_id" int4)
# 
# @brief 
#
# @param pid:int
# @param fid:int
#
# @return 
def delete_upvote(pid:int, fid:int):
    params = (pid, fid)
    exec_pro(SE, "delete_upvote", params)


##
# "StackExchange"."delete_user"
#   ("field_id" int4, "user_id" int4)
# 
# @brief 
#
# @param fid:int
# @param uid:int
#
# @return 
def delete_user(fid:int, uid:int):
    params = (fid, uid)
    exec_pro(SE, "delete_user", params)

##
# "StackExchange"."downvote"
#   ("post_id" int4, "field_id" int4)
# 
# @brief 
#
# @param pid:int
# @param fid:int
#
# @return 
def downvote(pid:int, fid:int):
    params = (pid, fid)
    exec_pro(SE, "downvote", params)

##
# "StackExchange"."remove_tag"
#   ("field_id" int4, "post_id" int4, "tag" text)
# 
# @brief  刪除一個 tag
#
# @param fid:int
# @param pid:int
# @param tag:String
#
# @return 
def remove_tag(fid:int, pid:int, tag:String):
    params = (fid, pid, tag)
    exec_pro(SE,"remove_tag",params)

##
# "StackExchange"."star_post"
#   ("post_id" int4, "user_id" int4, "field_id" int4)
# 
# @brief 收藏
#
# @param pid:int
# @param uid:int
# @param fid:int
#
# @return 
def star_post(pid:int, uid:int, fid:int):
    params = (pid, uid, fid)
    exec_pro(SE, "star_post", params)

##
# "StackExchange"."unstar_post"
#   ("post_id" int4, "user_id" int4, "field_id" int4)
#
# @brief 收藏？ 
#
# @param pid:int
# @param uid:int
# @param fid:int
#
# @return 
def unstar_post(pid:int, uid:int, fid:int):
    params = (pid, uid, fid)
    exec_pro(SE, "unstar_post", params)


##
# @brief 點讚
#
# @param pid:int
# @param fid:int
#
# @return 
def upvote(pid:int, fid:int):
    params = (pid, fid)
    exec_pro(SE, "upvote", params)
