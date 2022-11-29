"""
            Table "StackExchange.semantic_embeddings"
  Column   |        Type        | Collation | Nullable | Default
-----------+--------------------+-----------+----------+---------
 fieldid   | integer            |           | not null |
 postid    | integer            |           | not null |
 embedding | double precision[] |           | not null |
Indexes:
    "semantic_embeddings_pkey" PRIMARY KEY, btree (fieldid, postid)
Foreign-key constraints:
    "semantic_embeddings_fieldid_fkey" FOREIGN KEY (fieldid) REFERENCES "Common".fields(fieldid) ON DELETE CASCADE
    "semantic_embeddings_fieldid_postid_fkey" FOREIGN KEY (fieldid, postid) REFERENCES "StackExchange".posts(fieldid, id) ON DELETE CASCADE

"""
from . import db
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION

class SemanticEmbeddings(db.Model):
    __tablename__ = "semantic_embeddings"
    __table_args__ = {"schema": "StackExchange"}

    fieldid   =db.Column(db.Integer, nullable = True, primary_key = True)
    postid    =db.Column(db.Integer, nullable = True, primary_key = True)
    embedding =db.Column(db.ARRAY(DOUBLE_PRECISION), nullable = True)

    def __repr__(self):
        return f"<semantic_embeddings: {self.fieldid}: {self.postid}>"
