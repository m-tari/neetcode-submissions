class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pairs = {} # value -> counts
        for num in nums:
            if num in pairs:
                return True
            else:
                pairs[num] = 1
        return False
         