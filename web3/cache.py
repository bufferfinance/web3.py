import json
import os
import diskcache

disk_cache = diskcache.Cache("web3_cache")

def force_refresh_cache(f, *args, **kwargs):
    key = f.__cache_key__(*args, **kwargs)
    disk_cache.delete(key)
    return f(*args, **kwargs)