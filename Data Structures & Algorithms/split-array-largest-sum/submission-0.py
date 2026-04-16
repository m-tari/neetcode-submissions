class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        best = r 

        while l <= r:
            m = (l + r) // 2
            rsum = 0
            split = 1

            for num in nums:
                if rsum + num > m:
                    split +=1
                    rsum = num
                else:
                    rsum += num

            if split > k:
                l = m + 1
            elif split <= k:
                r = m - 1
                best = min(m, best)

        return best
