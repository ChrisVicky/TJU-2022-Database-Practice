"""
             Table "StackExchange.tags"
 Column  |  Type   | Collation | Nullable | Default
---------+---------+-----------+----------+---------
 fieldid | integer |           | not null |
 id      | integer |           | not null |
 tagname | text    |           |          |
 count   | integer |           |          |
Indexes:
    "tags_pkey" PRIMARY KEY, btree (fieldid, id)
Foreign-key constraints:
    "tags_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid)
Referenced by:
    TABLE ""StackExchange".post_tags" CONSTRAINT "post_tags_fieldid_tagid_fkey" FOREIGN KEY (fieldid, tagid) REFERENCES "StackExchange".tags(fieldid, id) ON DELETE CASCADE
"""

from . import db

class Tags(db.Model):
    __tablename__ = "tags"
    __table_args__ = {"schema": "StackExchange"}
    fieldid = db.Column(db.Integer, nullable=False, primary_key=True)
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    tagname = db.Column(db.Text)
    count = db.Column(db.Integer)

    def __repr__(self):
        return f'<Tags, {self.id} : {self.tagname}>'


    
