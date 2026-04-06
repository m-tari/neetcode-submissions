class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                sum =  nums[j] + nums[k]
                if sum  == target:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j]  == nums[k]:
                        k -= 1
                        j += 1
                if  sum > target:
                    k -= 1
                    while nums[k]  == nums[k + 1]:
                        k -= 1
                elif sum < target:
                    j += 1
                    while nums[j]  == nums[j - 1]:
                        j += 1  

        return res