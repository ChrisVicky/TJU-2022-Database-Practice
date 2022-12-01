from flask import Blueprint, render_template, request
from api.service import SearchService
import numpy as np
try:
    from utils.ML import get_emb, cos_sim
except:
    from utils.ML.get_semantic import get_embedding as get_emb
    from utils.ML.get_semantic import cos_sim
from pathlib import Path
import time
import pickle

searchpage = Blueprint('searchpage', __name__)


class CacheTable:
    def __init__(self, cache_size, embedding_len, hit_threshold=0.8):
        self.cache_size = cache_size
        self.embedding_len = embedding_len
        self.hit_threshold = hit_threshold
        Path("cached_search").mkdir(parents=True, exist_ok=True)
        if not self.load_cache():
            self.cache = np.zeros((cache_size, 1 + 1 + embedding_len))  # valid bit, LRU, embedding
            np.save("cached_search/cache.npy", self.cache)

    def save_cache(self):
        np.save("cached_search/cache.npy", self.cache)

    def load_cache(self):
        try:
            self.cache = np.load("cached_search/cache.npy")
            return True
        except Exception:
            return False

    def refresh_LRU(self, idx):
        """
        It updates the LRU of the cache table entry at index `idx` to the current time

        :param idx: the index of the cache table
        """
        current_time = int(time.time())
        # update LRU
        self.cache[idx][1] = current_time

    def evict(self):
        """
        It finds the oldest post in the cache table and returns its index
        :return: The index of the post to be evicted.
        """
        evict_idx = None
        for i in range(self.cache.shape[0]):
            if self.cache[i][0] == 0:  # is invalid
                evict_idx = i
                break
        if evict_idx is None:  # if no invalid post
            for i in range(self.cache.shape[0]):
                if self.cache[i][1] < self.cache[evict_idx][1]:  # find the oldest post
                    evict_idx = i
        self.cache[evict_idx][0] = 0
        return evict_idx

    def cache_post(self, embedding, posts):
        # add to cache table
        evict_idx = self.evict()
        self.cache[evict_idx][0] = 1  # valid
        self.cache[evict_idx][2:] = embedding
        self.refresh_LRU(evict_idx)
        # serialize posts using pickle
        Path(f"cached_search/{evict_idx}.pkl").write_bytes(pickle.dumps(posts))

    def cached_search(self, query: str, num: int):
        hit = False

        query_embedding = get_emb([query])[0]
        sim = cos_sim(query_embedding, self.cache[:, 2:])
        sim = sim.reshape(-1)
        similarest_idx = 0
        for i in range(self.cache.shape[0]):  # find the most similar post idx
            if self.cache[i][0] == 1 and sim[i] > sim[similarest_idx]:  # valid and most similar
                similarest_idx = i
        if sim[similarest_idx] > self.hit_threshold:  # if most similar post is similar enough
            cached_post_path = Path(f"cached_search/{similarest_idx}.pkl")
            if cached_post_path.exists():  # Hit
                self.refresh_LRU(similarest_idx)
                # deserialize posts using pickle
                posts = pickle.loads(cached_post_path.read_bytes())
                hit = True
                return hit, 0, posts
            else:
                self.cache[similarest_idx][0] = 0  # invalidate the post

        # Miss
        hit = False
        status, posts = SearchService.getSearchResult(query, num)
        if status == 0:
            self.cache_post(query_embedding, posts)

        self.save_cache()

        return hit, status, posts


cache_table = CacheTable(100, 384, 0.9)

##
# @brief Search Posts titles
@searchpage.route('/', methods=('GET', 'POST'))
def searchPage():
    if request.method == 'POST':
        content = request.form['content']
        hit, errorcode, posts = cache_table.cached_search(content, 10)
        if request.form.get('use_cached', 'off') == 'on':
            print("Using cached search")
        else:
            if hit:  # if hit, and we don't want to use cached search
                errorcode, posts = SearchService.getSearchResult(content, 12)
            else:  # cache miss, we can pretend nothing happened
                pass
        if errorcode:
            return render_template('500.html', msg=posts)
        return render_template('results.html', posts=posts, content=content)
    return render_template('search.html')
