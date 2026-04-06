class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, comb, total):
            if i >= len(nums) or total > target:
                return

            if total == target:
                res.append(comb.copy())
                return

            for j in range(i, len(nums)):
                comb.append(nums[j])
                dfs(j, comb, total + nums[j])
                comb.pop()

        dfs(0, [], 0)

        return res