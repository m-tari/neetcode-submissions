from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.mp = OrderedDict()

    def get(self, key: int) -> int:
        val = self.mp.get(key, -1)
        if val != -1:
            self.mp.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if len(self.mp) == self.size and key not in self.mp:
            self.mp.popitem(last=False)
        if key in self.mp:
            self.mp.move_to_end(key)
        self.mp[key] = value
