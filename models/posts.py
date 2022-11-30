"""
                   Table "StackExchange.posts"
        Column         |  Type   | Collation | Nullable | Default
-----------------------+---------+-----------+----------+---------
 fieldid               | integer |           | not null |
 id                    | integer |           | not null |
 posttypeid            | integer |           |          |
 acceptedanswerid      | integer |           |          |
 creationdate          | integer |           |          |
 score                 | integer |           |          |
 viewcount             | integer |           |          |
 body                  | text    |           |          |
 owneruserid           | integer |           |          |
 lasteditoruserid      | integer |           |          |
 lasteditdate          | integer |           |          |
 lastactivitydate      | integer |           |          | 
 title                 | text    |           |          | 
 tags                  | text    |           |          |
 answercount           | integer |           |          |
 commentcount          | integer |           |          |
 favoritecount         | integer |           |          |
 contentlicense        | text    |           |          |
 parentid              | integer |           |          |
 closeddate            | integer |           |          |
 communityowneddate    | integer |           |          |
 lasteditordisplayname | text    |           |          |
 ownerdisplayname      | text    |           |          |
Indexes:
    "posts_pkey" PRIMARY KEY, btree (fieldid, id)
Check constraints:
    "posts_content_length" CHECK (char_length(body) <= 60000)
    "posts_content_not_empty" CHECK (body <> ''::text)
Foreign-key constraints:
    "fieldid_acc_ans_id_fk" FOREIGN KEY (fieldid, acceptedanswerid) REFERENCES "StackExchange".posts(fieldid, id)
    "fieldid_fk" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid) ON DELETE CASCADE
    "fieldid_last_editor_id_fk" FOREIGN KEY (fieldid, lasteditoruserid) REFERENCES "StackExchange".users(fieldid, id)
    "fieldid_owner_id_fk" FOREIGN KEY (fieldid, owneruserid) REFERENCES "StackExchange".users(fieldid, id)
    "fieldid_parent_id_fk" FOREIGN KEY (fieldid, parentid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
Referenced by:
    TABLE ""StackExchange".comments" CONSTRAINT "comments_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".posts" CONSTRAINT "fieldid_acc_ans_id_fk" FOREIGN KEY (fieldid, acceptedanswerid) REFERENCES "StackExchange".posts(fieldid, id)
    TABLE ""StackExchange".posts" CONSTRAINT "fieldid_parent_id_fk" FOREIGN KEY (fieldid, parentid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".post_tags" CONSTRAINT "post_tags_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".posthistory" CONSTRAINT "posthistory_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".postlinks" CONSTRAINT "postlinks_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE SET NULL
    TABLE ""StackExchange".postlinks" CONSTRAINT "postlinks_fieldid_relatedpostid_fkey" FOREIGN KEY (fieldid, relatedpostid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE SET NULL
    TABLE ""StackExchange".user_starred" CONSTRAINT "user_starred_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE
CASCADE
    TABLE ""StackExchange".votes" CONSTRAINT "votes_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
Triggers:
    post_history_trigger AFTER UPDATE ON "StackExchange".posts FOR EACH ROW EXECUTE FUNCTION "StackExchange".post_history_trigger_proc()
    posts_fk_trigger BEFORE DELETE ON "StackExchange".posts FOR EACH ROW EXECUTE FUNCTION "StackExchange".posts_fk_trigger_proc()
    posts_profanity_trigger BEFORE INSERT OR UPDATE ON "StackExchange".posts FOR EACH ROW EXECUTE FUNCTION "StackExchange".posts_profanity_trigger_proc()
"""

from . import db

class Posts(db.Model):
    __tablename__ = "posts"
    __table_args__ = {"schema": "StackExchange"}

    fieldid               = db.Column(db.Integer, primary_key=True)
    id                    = db.Column(db.Integer, primary_key=True)
    posttypeid            = db.Column(db.Integer)
    acceptedanswerid      = db.Column(db.Integer)
    creationdate          = db.Column(db.Integer)
    score                 = db.Column(db.Integer)
    viewcount             = db.Column(db.Integer)
    body                  = db.Column(db.Text   )
    owneruserid           = db.Column(db.Integer)
    lasteditoruserid      = db.Column(db.Integer)
    lasteditdate          = db.Column(db.Integer)
    lastactivitydate      = db.Column(db.Integer)
    title                 = db.Column(db.Text   )
    tags                  = db.Column(db.Text   )
    answercount           = db.Column(db.Integer)
    commentcount          = db.Column(db.Integer)
    favoritecount         = db.Column(db.Integer)
    contentlicense        = db.Column(db.Text   )
    parentid              = db.Column(db.Integer)
    closeddate            = db.Column(db.Integer)
    communityowneddate    = db.Column(db.Integer)
    lasteditordisplayname = db.Column(db.Text   )
    ownerdisplayname      = db.Column(db.Text   )

    def __repr__(self) -> str:
        return  f"< post: {self.fieldid, self.id}>"
    
