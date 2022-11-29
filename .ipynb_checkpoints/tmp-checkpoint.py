from utils import log, tag2tag
from models.procedures import add_tag
from models.posts import Posts
from sqlalchemy import update
from models import db
from utils.get_semantic import get_embedding
from models.semantic_embeddings import SemanticEmbeddings
from models.fpid_cache import FpidCache
from utils import fu_in_one
##
# @brief Move all tags in table posts to table tags without removing tag columns
#
# @return 
def moveTags():
    log("move tag start")
    total_num = Posts.query.filter(Posts.tags!=None).count()
    log(f"total posts: {total_num}")
    limit = 10
    total_num = int(total_num/limit) + 1
    erc = 0
    for offset in range(total_num):
        posts = Posts.query.filter(Posts.tags!=None).limit(limit).offset(offset*limit).all()
        lenpost = len(posts)
        for i,p in enumerate(posts):
            tags = p.tags
            tags = tag2tag(tags)
            total = len(tags)
            for index, t in enumerate(tags):
                try:
                    add_tag(p.fieldid, p.id, t)
                    # log(f"tag added {index}/{total}")
                except Exception as e:
                    log(f"debug: {t}, {p.fieldid}, {p.id}")
                    log(f"{e}")
                    erc = erc + 1
                    pass
            p.tags = None
        db.session.commit()
        log(f"post dealt  {offset}/{total_num} - erc: {erc}")



# TODO: NONONONONONONO DONE
##
# @brief 
#
# @return 
def insert_embeddings():
    log("start embedding insertion")
    total_num = Posts.query.filter(Posts.title!=None).count()
    log(f"Total {total_num}")
    limit = 10
    total_num = int(total_num/limit)+1
    erc = 0
    for offset in range(total_num):
        posts = Posts.query.filter(Posts.title!=None).limit(limit).offset(offset*limit).all()
        titles = [p.title for p in posts]
        titles_em = get_embedding(titles)
        for index,p in enumerate(posts):
            try:
                segm = SemanticEmbeddings.query.filter(SemanticEmbeddings.fieldid==p.fieldid, SemanticEmbeddings.postid==p.id).first()
                if segm is not None:
                    log(f"{p.fieldid}, {p.id} embeded before")
                    continue
                input = SemanticEmbeddings(fieldid=p.fieldid, postid=p.id, embedding=titles_em[index])
                db.session.add(input)
            except Exception as e:
                log(f"debug: {p.fieldid}, {p.id}, {titles_em[index].shape}")
                log(f"{e}")
                erc = erc + 1
                pass
        db.session.commit()
        log(f"{offset}/{total_num} erc: {erc}")

