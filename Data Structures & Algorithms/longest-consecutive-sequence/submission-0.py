class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        inits = []
        for num in nums:
            if num - 1 not in numsSet:
                inits.append(num)
        
        res = 0
        for init in inits:
            l = 1
            while init + 1 in numsSet:
                l += 1
                init += 1
            res = max(l, res)

        
        return res