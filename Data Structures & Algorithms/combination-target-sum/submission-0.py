class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, comb):
            if i >= len(nums) or sum(comb) > target:
                return

            if sum(comb) == target:
                self.res.append(comb[:])
                return

            comb.append(nums[i])
            dfs(i, comb)
            comb.pop()

            dfs(i + 1, comb)

        dfs(0, [])

        return self.res