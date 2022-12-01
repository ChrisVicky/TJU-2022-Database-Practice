from sentence_transformers import SentenceTransformer
import numpy as np
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_emb(sentence_list:list[str]):
    embeddings = model.encode(sentence_list)
    return embeddings.astype(np.float64)
    # return np.array(embeddings)

def cos_sim(a: np.ndarray, b: np.ndarray):
    """
    Computes the cosine similarity cos_sim(a[i], b[j]) for all i and j.
    :return: Similarity matrix with res[i][j]  = cos_sim(a[i], b[j])
    """
    if len(a.shape) == 1:
        a = a[np.newaxis, :]

    if len(b.shape) == 1:
        b = b[np.newaxis, :]

    a_norm = np.linalg.norm(a, axis=1, keepdims=True)
    b_norm = np.linalg.norm(b, axis=1, keepdims=True)
    return np.dot(a / a_norm, (b / b_norm).T)