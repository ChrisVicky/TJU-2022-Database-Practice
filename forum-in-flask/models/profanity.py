"""
                                        Table "Common.profanity"
 Column |          Type          | Collation | Nullable |                    Default
--------+------------------------+-----------+----------+------------------------------------------------
 id     | integer                |           | not null | nextval('"Common".profanity_id_seq'::regclass)
 word   | character varying(255) |           | not null |
Indexes:
    "profanity_pkey" PRIMARY KEY, btree (id)
"""

from . import db

class Profanity(db.Model):
    __tablename__ = "profanity"
    __table_args__ = {"schema":"Common"}
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    word = db.Column(db.String(255), nullable=False)

    def __repr__(self) :
        return f'<Profanity: [{self.id}: {self.word}]>'
