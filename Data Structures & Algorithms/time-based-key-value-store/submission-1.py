from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.mp.get(key):
            return ""

        values = self.mp[key]
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = (r + l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1

        return res
