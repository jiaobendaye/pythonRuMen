# coding utf-8
"""
生成一个字增长的连续数字
这个数字可能会失败 但是失败后要优先再次使用
要求 不重复 效率高 1000的并发
隔夜重置 服务重启不丢失

"""
from datetime import datetime
from django_redis import  get_redis_connection
from redis import Redis

def _get_daily_key() -> str:
    day = datetime.now().strftime('%Y-%m-%d')
    return f"{day}_no"

def _get_failed_seq_key() -> str:
    prefix = _get_daily_key()
    return f"{prefix}_failed"

def next_no() -> int:
    redis : Redis = get_redis_connection()
    key = _get_daily_key()
    seq_key = _get_failed_seq_key()
    no = redis.lpop(seq_key)
    if no:
        return int(no)
    
    no = redis.incr(key)
    return int(no)

def report_failed_no(no:int):
    redis: Redis = get_redis_connection()
    redis.lpush(_get_failed_seq_key(), no)

