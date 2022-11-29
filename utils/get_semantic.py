##
# @file get_semantic.py
# @brief Deprecated -- API is not free
# @author Christopher Liu
# @version 1.0
# @date 2022-11-29


import requests
from retry import retry
import numpy as np
from typing import List

model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"

api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}


@retry(tries=5, delay=20)
##
# @brief Deprecated
#
# @param List[str]
#
# @return 
def get_embedding(texts: List[str]) -> np.ndarray:
    """
    Query the API for embeddings
    :param texts: a list of texts, each text is a string: List[str]
    :return: a numpy array of shape (len(texts), 384)
    """
    response = requests.post(api_url, headers=headers, json={"inputs": texts})
    result = response.json()
    if isinstance(result, list):
        return np.array(result)
    elif list(result.keys())[0] == "error":
        raise RuntimeError(result["error"])


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


if __name__ == "__main__":
    textss = ["I like apples",
              "I like oranges",
              "Did you do your homework?",
              "What did the teacher say?",
              "What's the homework?",
              "What's deadline of homework?"]

    output = get_embedding(textss)
    print(output)

    embedding_str = str(output[0].tolist())
    field_id = 1
    post_id = 431177
    print(f"VALUES({field_id},{post_id},'{{{embedding_str[1:-1]}}}');")

    # # draw a similarity matrix
    # import matplotlib.pyplot as plt
    # import seaborn as sns
    #
    # sim_matrix = cos_sim(output, output)
    # plt.rcParams["figure.figsize"] = (20, 20)
    # sns.heatmap(sim_matrix, annot=True, xticklabels=textss, yticklabels=textss)
    # plt.show()
