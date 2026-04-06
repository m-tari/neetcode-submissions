class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def solve(arr):
            rob, rob_p, rob_pp = 0, 0, 0
            for num in arr:
                rob = max(rob_p, rob_pp + num)
                rob_pp = rob_p
                rob_p = rob 
               
            return rob

        return max(nums[0], solve(nums[1:]), solve(nums[:-1])) 