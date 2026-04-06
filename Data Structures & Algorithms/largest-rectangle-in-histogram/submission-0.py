class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        n = len(heights)
        l, r = [0]* n, [0] * n  # index of right and left side of the rectangle formed by current h, inclusive

        l[0] = 0
        for i in range(1, n):
            if  heights[i] > heights[i - 1]:
                l[i] = i
            else:
                l[i] = l[i - 1]
            
        r[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if  heights[i] > heights[i + 1]:
                r[i] = i
            else:
                r[i] = r[i + 1]

        A = 0
        for i in range(n):
            A = max(A, heights[i] * (r[i] - l[i] + 1) )

        return A