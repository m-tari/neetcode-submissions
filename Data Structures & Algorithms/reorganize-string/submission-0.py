from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = defaultdict(int)
        maxHeap = []

        for c in s:
            counts[c] += 1
        
        for char, count in counts.items():
            heapq.heappush(maxHeap, [-count, char])

        res = []
        n = len(s)

        while True:
            if not maxHeap:
                return "".join(res)
                
            maxCount, maxChar = heapq.heappop(maxHeap)
            if res and maxChar == res[-1]:
                if not maxHeap:
                    return ""
                count, char  = heapq.heappop(maxHeap)
                res.append(char)
                if count + 1 != 0:
                    heapq.heappush(maxHeap, [count+1, char])
            else:
                res.append(maxChar)
                maxCount += 1
            if maxCount != 0:
                heapq.heappush(maxHeap, [maxCount, maxChar])



