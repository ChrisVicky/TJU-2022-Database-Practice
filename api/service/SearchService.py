from utils.ML import get_emb
from models.functions import semantic_query
from utils import log
from models.semantic_embeddings import SemanticEmbeddings
from api.service import PostService

def getSearchResult(content:str, num:int):
    try:
        emb = get_emb([content])[0]
        log(f"Embeded Success: {emb.shape}")
        result = semantic_query(num, emb.tolist())
        posts = PostService.getPostsBySearch(result)
        return 0, posts
    except Exception as e:
        raise e
        return 1, e


