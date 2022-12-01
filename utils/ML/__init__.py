try:
    from .embedding_module import get_emb, cos_sim
except:
    from .get_semantic import get_embedding as get_emb
    from .get_semantic import cos_sim