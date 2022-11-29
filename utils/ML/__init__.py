from sentence_transformers import SentenceTransformer
import numpy as np
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_emb(sentence_list:list[str]):
    embeddings = model.encode(sentence_list)
    return embeddings.astype(np.float64)
    # return np.array(embeddings)

