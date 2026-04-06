import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        maxHeap = []

        for point in points:
            d = sqrt(point[0]**2 + point[1]**2)
            if len(maxHeap) == k:
                maxD, maxPoint = maxHeap[0]
                if d < -1*maxD:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-d, point))
            else:
                heapq.heappush(maxHeap, (-d, point))

        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res