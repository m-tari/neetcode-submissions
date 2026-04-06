import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        count = 0
        end = -float("inf")
        
        for i in intervals:
            if i[0] < end:
                end = min(i[1], end)
                count += 1
            if i[0] > end and i[1] > end:
                end = i[1]

        return count

        #     []                 
        #   [    ][  ]              [       ]
        # [               ] [           ][               ]