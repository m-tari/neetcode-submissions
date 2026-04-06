class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        set_nums = sorted(self.nums, reverse=True)
        print(set_nums)
        if len(set_nums[self.k - 1:self.k]) != 0:
            res = set_nums[self.k - 1]
        elif set_nums[0:1]:
            res = set_nums[0]
        else:
            res = None
        return res
        
