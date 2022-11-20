"""
                                 Table "Common.fields"
   Column    |  Type   | Collation | Nullable |                 Default
-------------+---------+-----------+----------+-----------------------------------------
 fieldid     | integer |           | not null | nextval('fields_fieldid_seq'::regclass)
 description | text    |           |          |
Indexes:
    "fields_pkey" PRIMARY KEY, btree (fieldid)
Referenced by:
    TABLE "badges" CONSTRAINT "badges_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "comments" CONSTRAINT "comments_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "posts" CONSTRAINT "fieldid_fk" FOREIGN KEY (fieldid) REFERENCES fields(fieldid) ON DELETE CASCADE
    TABLE "post_tags" CONSTRAINT "post_tags_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid) ON DELETE CASCADE
    TABLE "posthistory" CONSTRAINT "posthistory_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "postlinks" CONSTRAINT "postlinks_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "tags" CONSTRAINT "tags_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "user_bans" CONSTRAINT "user_bans_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid) ON DELETE CASCADE
    TABLE "user_credentials" CONSTRAINT "user_credentials_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid) ON DELETE
    TABLE "user_starred" CONSTRAINT "user_starred_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "users" CONSTRAINT "users_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
    TABLE "votes" CONSTRAINT "votes_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES fields(fieldid)
"""

from . import db

class Fields(db.Model):
    __tablename__ = "fields"
    __table_args__ = {"schema": "Common"}
    fieldid = db.Column(db.Integer, nullable=False, primary_key=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Fiels: {self.fieldid}>'



