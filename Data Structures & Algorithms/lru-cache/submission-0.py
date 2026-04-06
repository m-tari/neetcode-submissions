from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.q = deque([])
        self.mp = {}

    def get(self, key: int) -> int:
        return self.mp.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.q) == self.size:
            LRUkey = self.q.popleft()
            self.mp.pop(LRUkey)
        self.mp[key] = value
        self.q.append(key)
