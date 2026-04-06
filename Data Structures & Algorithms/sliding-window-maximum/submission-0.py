import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxHeap = []
        l, r = 0, k -1
        res = []

        i = 0
        while i < k - 1:
            heapq.heappush(maxHeap,( -1*nums[i], i))
            i += 1 

        while r < n:
            heapq.heappush(maxHeap, (-1*nums[r], r))
            maxN, pos = heapq.heappop(maxHeap)
            while  pos < l or pos > r:
                maxN, pos = heapq.heappop(maxHeap)
            res.append(-1*maxN)
            heapq.heappush(maxHeap, (maxN, pos))
            l += 1
            r += 1


        return res
