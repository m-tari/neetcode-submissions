class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        i = 0
        jamx = 0
        while i < len(nums) - 1:
            maxr = nums[i]
            jmax = 0
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) - 1:
                    r = j + nums[i + j]
                else:
                    step += 1
                    return step
                if r > maxr:
                    jmax = j
                    maxr = r
            i += jmax
            step += 1

        return step

        