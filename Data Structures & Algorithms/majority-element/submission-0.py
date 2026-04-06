from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        majCount = len(nums) // 2

        for num in nums:
            count[num] += 1
            if count[num] > majCount:
                return num
