"""
          Table "StackExchange.post_tags"
 Column  |  Type   | Collation | Nullable | Default
---------+---------+-----------+----------+---------
 fieldid | integer |           | not null |
 postid  | integer |           | not null |
 tagid   | integer |           | not null |
Indexes:
    "post_tags_pkey" PRIMARY KEY, btree (fieldid, postid, tagid)
Foreign-key constraints:
    "post_tags_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid) ON DELETE CASCADE
    "post_tags_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE
    "post_tags_fieldid_tagid_fkey" FOREIGN KEY (fieldid, tagid) REFERENCES "StackExchange".tags(fieldid, id) ON DELETE CASCADE
"""
from . import db

class PostTags(db.Model):
    __tablename__ = "post_tags"
    __table_args__ = {"schema": "StackExchange"}
    fieldid = db.Column(db.Integer, primary_key=True)
    postid  = db.Column(db.Integer, primary_key=True)
    tagid   = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<PostTags: {self.fieldid}, {self.postid}, {self.tagid}>'




