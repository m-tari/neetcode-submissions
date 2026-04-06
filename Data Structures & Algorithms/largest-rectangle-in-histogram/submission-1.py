class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        n = len(heights)
        stack = [] # indices in increasing h order

        maxA = 0
        for i, h in enumerate(heights + [0]):
            while stack and  h < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]
                # The right boundary is i (exclusive)
                # The left boundary is the element currently at the top of the stack (exclusive)
                right = i
                # Go back to the beginning of the array
                if not stack:
                    left = 0
                else:
                    left = stack[-1] + 1

                width = right - left
                maxA = max(maxA, height * width)
            stack.append(i)
        
        return maxA

#                       i
#        [4, 5, 6 , 3, 4, 5, 2, 1]


