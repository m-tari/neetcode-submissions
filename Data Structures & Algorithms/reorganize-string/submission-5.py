from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        maxHeap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(maxHeap)

        res = []
        while True:
            if not maxHeap:
                return "".join(res)
                
            maxCount, maxChar = heapq.heappop(maxHeap)
            if res and maxChar == res[-1]:
                if not maxHeap:
                    return ""
                count, char  = heapq.heappop(maxHeap)
                res.append(char)
                count += 1
                if count  !=  0:
                    heapq.heappush(maxHeap, [count, char])
            else:
                res.append(maxChar)
                maxCount += 1
            if maxCount != 0:
                heapq.heappush(maxHeap, [maxCount, maxChar])



