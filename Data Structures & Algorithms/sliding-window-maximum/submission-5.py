import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxHeap = []
        res = []

        for i in range(n):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                while  maxHeap[0][1] <= i - k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])

        return res
