import time


class SimpleCache:

    def __init__(self):
        self.storage = {}

    def get(self, key):
        if key not in self.storage:
            return None

        value, expiry = self.storage[key]

        if time.time() > expiry:
            del self.storage[key]
            print(f"[CACHE EXPIRED] {key}")
            return None

        print(f"[CACHE HIT] {key}")
        return value

    def set(self, key, value, ttl=60):
        self.storage[key] = (
            value,
            time.time() + ttl,
        )

        print(f"[CACHE STORE] {key}")


cache = SimpleCache()