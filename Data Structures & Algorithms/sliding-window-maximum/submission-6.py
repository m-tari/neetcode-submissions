from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        l, r = 0, 0

        while r < n:

            # Remove smaller items
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Out of left band of the window
            if q[0] < l:
                q.popleft()

            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
