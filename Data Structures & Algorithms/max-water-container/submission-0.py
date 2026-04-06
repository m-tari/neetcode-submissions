class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        l, r = 0, N -1 

        max_area = 0
        while r > l:
            max_area = max(max_area, (r - l) * (min(heights[l], heights[r])))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_area