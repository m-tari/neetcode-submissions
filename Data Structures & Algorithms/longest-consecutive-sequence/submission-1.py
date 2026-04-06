class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        inits = []
        for num in nums:
            if num - 1 not in numSet:
                inits.append(num)
        
        longest = 0
        for init in inits:
            streak = 1
            while (init + 1) in numSet:
                streak += 1
                init += 1
            longest = max(streak, longest)

        
        return longest