class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r 

        while l <= r:
            m = (l + r) // 2
            curSum = 0
            split = 1

            for num in nums:
                if curSum + num > m:
                    split +=1
                    curSum = num
                else:
                    curSum += num

            if split > k:
                l = m + 1
            elif split <= k:
                r = m - 1
                # m is one possible solution. We adjust r to see if we can do better by finding a smaller value
                res = m

        return res
