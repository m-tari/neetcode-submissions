class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        totalProd = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                totalProd *= num
    
            if zeroCount == 2:
                return output

        for i, num in enumerate(nums):
            if zeroCount:
                output[i] = 0 if num else totalProd
            else:
                output[i] = totalProd // num

        return output