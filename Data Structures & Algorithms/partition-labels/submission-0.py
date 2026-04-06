from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(dict)

        for i, c in enumerate(s):
            last[c] = i

        res = []
        size = 0
        maxLast = 0
        for i, c in enumerate(s):
            maxLast = max(maxLast, last[c])
            size += 1
            if i == maxLast :
                res.append(size)
                size = 0

        return res