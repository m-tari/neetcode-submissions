class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1

        return jumps


#             l          r  
# [ 2, 6, 4, 7, 9, 5, 1, 0, 2]
        