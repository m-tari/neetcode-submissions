import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxHeap = []
        res = []

        for i in range(n):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                maxN, pos = maxHeap[0]
                while  pos <= i - k:
                    heapq.heappop()
                res.append(-maxN)

        return res
