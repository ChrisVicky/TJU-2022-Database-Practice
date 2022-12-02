"""
       Table "StackExchange.user_credentials"
  Column  |  Type   | Collation | Nullable | Default
----------+---------+-----------+----------+---------
 fieldid  | integer |           | not null |
 userid   | integer |           | not null |
 username | text    |           | not null |
 password | text    |           | not null |
Indexes:
    "user_credentials_pkey" PRIMARY KEY, btree (username)
    "user_credentials_userid_key" UNIQUE CONSTRAINT, btree (userid)
Foreign-key constraints:
    "user_credentials_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid) ON DELETE CASCADE
    "user_credentials_fieldid_userid_fkey" FOREIGN KEY (fieldid, userid) REFERENCES "StackExchange".users(fieldid, id) ON DELETE CASCADE
"""

from . import db


class UserCredentials(db.Model):
    __tablename__ = "user_credentials"
    __table_args__ = {"schema":"StackExchange"}
    fieldid  =db.Column(db.Integer ,nullable=True, primary_key=True) 
    userid   =db.Column(db.Integer ,nullable=True, primary_key=True)
    username =db.Column(db.Text    ,nullable=True)
    password =db.Column(db.Text    ,nullable=True)

    def __repr__(self) :
        return f'<user credentials: [{self.fieldid}: {self.userid}]>'

