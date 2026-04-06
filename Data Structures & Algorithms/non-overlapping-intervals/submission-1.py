import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        count = 0
        last_end = -float("inf")
        
        for start, end in intervals:
            # Overlap detected
            if start < last_end:
                last_end = min(last_end, end)
                count += 1
            # No overlap
            if start >= last_end:
                last_end = end

        return count

        #     []                 
        #   [    ][  ]              [       ]
        # [               ] [           ][               ]