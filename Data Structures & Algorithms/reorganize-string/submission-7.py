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
                
            count1, char1 = heapq.heappop(maxHeap)

            if res and char1 == res[-1]:
                if not maxHeap:
                    return ""

                count2, char2  = heapq.heappop(maxHeap)
                res.append(char2)
                count2 += 1

                if count2  !=  0:
                    heapq.heappush(maxHeap, [count2, char2])

                heapq.heappush(maxHeap, [count1, char1])
            else:
                res.append(char1)
                count1 += 1
                if count1 != 0:
                    heapq.heappush(maxHeap, [count1, char1])



