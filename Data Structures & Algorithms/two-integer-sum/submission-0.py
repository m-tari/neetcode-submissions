class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {} # value -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in pairs:
                return [pairs[diff], i]
            pairs[num] = i
        
        