"""
         View "StackExchange.top_score_posts_of_the_week"
        Column         |  Type   | Collation | Nullable | Default
-----------------------+---------+-----------+----------+---------
 fieldid               | integer |           |          |
 id                    | integer |           |          |
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
"""

from . import db

class Top(db.Model):
    __tablename__ = "top_score_posts_of_the_week"
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
        return  f"< top post: {self.fieldid, self.id}>"
    

