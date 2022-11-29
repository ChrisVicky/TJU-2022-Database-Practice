import datetime
import time

def translateTime(timeStamp):
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

def getCurretTime():
    return datetime.datetime.now()

def getCurrentTimeStamp():
    return int(time.time())

def log(msg):
    import sys
    tmp = sys._getframe(1)
    print(f"[{getCurretTime()}] [{tmp.f_code.co_name}:{tmp.f_lineno}] [{msg}]")
    
N = int(1e7)
def fu_in_one(fid:int, uid:int):
    return fid * N + uid

def u_from_fu(fuid:int):
    return fuid % N

def f_from_fu(fuid:int):
    return int(fuid/N)



"""
<deep-learning><convolutional-neural-networks><pooling><max-pooling>
"""
def tag2tag(tags:str):
    tags = tags.replace('>', '')
    tags = tags[1:]
    ret = tags.split('<')
    return ret







