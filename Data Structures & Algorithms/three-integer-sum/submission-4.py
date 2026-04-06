class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if  nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                threeSum = nums[i] +  nums[j] + nums[k]
                if threeSum  == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[k]  == nums[k + 1]:
                        k -= 1
                    while j < k and nums[j]  == nums[j - 1]:
                        j += 1  
                if  threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
        return res