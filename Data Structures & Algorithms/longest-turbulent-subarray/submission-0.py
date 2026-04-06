class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0

        L = 0
        maxSize = 1
        curMaxSize = 1
        nextLess = True
        nextGreater = True
        
        for R in range(len(arr)):

            if R + 1 < len(arr):
                if arr[R + 1] > arr[R] and nextGreater:
                    curMaxSize +=1
                    nextLess, nextGreater = True, False
                elif arr[R + 1] < arr[R] and nextLess:
                    curMaxSize +=1
                    nextLess, nextGreater = False, True
                else:
                    curMaxSize = 1
                    L = R

            maxSize = max(maxSize, curMaxSize)

        return maxSize