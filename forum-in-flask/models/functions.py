##
# @file functions.py
# @brief Functions DeFined in Postgresql
# @author Christopher Liu
# @version 1.0
# @date 2022-11-30

from . import exec_func, db

# two schemas
SE = "StackExchange"
CM = "Common"

"""
"StackExchange".semantic_query(num integer, query_embedding double precision[])"
"""
def semantic_query(num, emb):
    try:
        session = db.engine.raw_connection().cursor()
        session.callproc("\"StackExchange\".semantic_query", [num,emb])
        results = list(session.fetchall())
        session.close()
        return results
    except Exception as e:
        raise e
    finally:
        session.close()

