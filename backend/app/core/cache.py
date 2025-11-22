from typing import Optional, Tuple
from collections import OrderedDict
import time
import asyncio
from fastapi_cache.backends import Backend

class LRUBackend(Backend):
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.cache: OrderedDict[str, Tuple[bytes, Optional[float]]] = OrderedDict()
        self.lock = asyncio.Lock()

    async def get_with_ttl(self, key: str) -> Tuple[int, Optional[bytes]]:
        async with self.lock:
            if key not in self.cache:
                return -1, None
            
            value, expire = self.cache[key]
            if expire is not None:
                ttl = int(expire - time.time())
                if ttl < 0:
                    del self.cache[key]
                    return -1, None
            else:
                ttl = -1
            
            self.cache.move_to_end(key)
            return ttl, value

    async def get(self, key: str) -> Optional[bytes]:
        async with self.lock:
            if key not in self.cache:
                return None
            
            value, expire = self.cache[key]
            if expire is not None and time.time() > expire:
                del self.cache[key]
                return None
            
            self.cache.move_to_end(key)
            return value

    async def set(self, key: str, value: bytes, expire: Optional[int] = None) -> None:
        async with self.lock:
            expiry = time.time() + expire if expire is not None else None
            
            if key in self.cache:
                self.cache.move_to_end(key)
            
            self.cache[key] = (value, expiry)
            
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)

    async def clear(self, namespace: Optional[str] = None, key: Optional[str] = None) -> int:
        async with self.lock:
            if namespace:
                keys_to_remove = [k for k in self.cache if k.startswith(namespace)]
                for k in keys_to_remove:
                    del self.cache[k]
                return len(keys_to_remove)
            elif key:
                 if key in self.cache:
                     del self.cache[key]
                     return 1
                 return 0
            else:
                count = len(self.cache)
                self.cache.clear()
                return count
