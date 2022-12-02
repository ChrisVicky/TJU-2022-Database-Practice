"""
             Table "StackExchange.comments"
    Column    |  Type   | Collation | Nullable | Default
--------------+---------+-----------+----------+---------
 fieldid      | integer |           | not null |
 id           | integer |           | not null |
 postid       | integer |           |          |
 score        | integer |           |          | 0
 text         | text    |           |          |
 creationdate | integer |           |          |
 userid       | integer |           |          |
Indexes:
    "comments_pkey" PRIMARY KEY, btree (fieldid, id)
Foreign-key constraints:
    "comments_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid)
    "comments_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    "comments_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE SET NULL
Triggers:
    comments_profanity_trigger BEFORE INSERT OR UPDATE ON "StackExchange".comments FOR EACH ROW EXECUTE FUNCTION "StackExchange".comments_profanity_trigger_proc()
"""
from . import db

class Comments(db.Model):
    __tablename__ = "comments"
    __table_args__ = {"schema": "StackExchange"}
    fieldid = db.Column(db.Integer, nullable=False, primary_key=True)
    id           = db.Column(db.Integer, primary_key=True)
    postid       = db.Column(db.Integer )
    score        = db.Column(db.Integer )
    text         = db.Column(db.Text    )
    creationdate = db.Column(db.Integer )
    userid       = db.Column(db.Integer )

    def __repr__(self):
        return f'<Comments: {self.id}>'
