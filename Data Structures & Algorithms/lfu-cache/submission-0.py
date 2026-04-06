from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> (value, freq)
        self.freq_map = defaultdict(OrderedDict)  #  freq -> [key], a group of keys with the same frequncy orderd by receny [LRU...MRU]
        # freq_map = {
        #     1: [k3, k5],
        #     2: [k1],
        #     3: [k2, k4]
        # }
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        val, freq = self.cache[key]
        
        # remove from current freq
        del self.freq_map[freq][key]
        
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        # add to next freq
        self.cache[key] = (val, freq + 1)
        self.freq_map[freq + 1][key] = None

        print(self.freq_map)
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key in self.cache:
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # reuse logic
            return
        
        if len(self.cache) >= self.cap:
            # evict LFU + LRU
            k, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[k]
        
        # insert new key
        self.cache[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1

        print(self.freq_map)
