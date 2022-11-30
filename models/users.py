"""
                                     Table "StackExchange.users"
     Column      |  Type   | Collation | Nullable |                      Default
-----------------+---------+-----------+----------+---------------------------------------------------
 fieldid         | integer |           | not null |
 id              | integer |           | not null | nextval('"StackExchange".users_id_seq'::regclass)
 reputation      | integer |           |          | 0
 creationdate    | integer |           |          |
 displayname     | text    |           |          |
 lastaccessdate  | integer |           |          |
 location        | text    |           |          |
 aboutme         | text    |           |          |
 views           | integer |           |          |
 upvotes         | integer |           |          |
 downvotes       | integer |           |          |
 accountid       | integer |           |          |
 profileimageurl | text    |           |          |
 websiteurl      | text    |           |          |
Indexes:
    "users_pkey" PRIMARY KEY, btree (fieldid, id)
Foreign-key constraints:
    "users_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid)
Referenced by:
    TABLE ""StackExchange".badges" CONSTRAINT "badges_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".comments" CONSTRAINT "comments_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE SET NULL
    TABLE ""StackExchange".posts" CONSTRAINT "fieldid_last_editor_id_fk" FOREIGN KEY (fieldid, lasteditoruserid) REFERENCES "StackExchange".users(fieldid, id)
    TABLE ""StackExchange".posts" CONSTRAINT "fieldid_owner_id_fk" FOREIGN KEY (fieldid, owneruserid) REFERENCES "StackExchange".users(fieldid, id)
    TABLE ""StackExchange".user_bans" CONSTRAINT "user_bans_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".user_credentials" CONSTRAINT "user_credentials_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE CASCADE
    TABLE ""StackExchange".user_starred" CONSTRAINT "user_starred_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE
CASCADE
Triggers:
    delete_user_credentials_trigger AFTER DELETE ON "StackExchange".users FOR EACH ROW EXECUTE FUNCTION "StackExchange".delete_user_credentials()
    users_fk_trigger BEFORE DELETE ON "StackExchange".users FOR EACH ROW EXECUTE FUNCTION "StackExchange".users_fk_trigger_proc()
    users_profanity_trigger BEFORE INSERT OR UPDATE ON "StackExchange".users FOR EACH ROW EXECUTE FUNCTION "StackExchange".users_profanity_trigger_proc()
"""

from . import db

class Users(db.Model):
    __tablename__   = "users"
    __table_args__ = {"schema": "StackExchange"}
    # NOTE: primary_key order matters (filedid, id) as a pair of KEY Refered by Other tables
    fieldid         = db.Column(db.Integer, nullable=False, primary_key=True)
    id              = db.Column(db.Integer, primary_key=True, nullable=False)

    reputation      = db.Column(db.Integer)
    creationdate    = db.Column(db.Integer)
    displayname     = db.Column(db.Text )
    lastaccessdate  = db.Column(db.Integer)
    location        = db.Column(db.Text )
    aboutme         = db.Column(db.Text )
    views           = db.Column(db.Integer)
    upvotes         = db.Column(db.Integer)
    downvotes       = db.Column(db.Integer)
    accountid       = db.Column(db.Integer)
    profileimageurl = db.Column(db.Text )
    websiteurl      = db.Column(db.Text )

    def __repr__(self):
        return f'<User: {self.id}: {self.fieldid}>'
