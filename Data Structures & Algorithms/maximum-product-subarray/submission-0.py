class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        maxProd = prod = 1
        for i, num in enumerate(nums):
            if not num:
                prod = 1
                continue
            if num < 0 and prod < 0:
                prod *= num
            if num < 0 and prod > 0:
                if i + 1 < len(nums):
                    if  nums[i+1] < 0:
                        prod *= num 
                    else:
                         prod = 1
            else:
                prod *= num

            maxProd = max(prod, maxProd)

        return maxProd
        