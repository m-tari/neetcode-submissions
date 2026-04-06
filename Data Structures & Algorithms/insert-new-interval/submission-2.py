from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        b_idx = 0
        a_idx = len(intervals)
        
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                b_idx = i + 1  # comes before newInterval
            elif interval[0] > newInterval[1]:
                a_idx = min(a_idx, i)  # comes after newInterval

        # No overlap — just insert
        if b_idx == a_idx:
            intervals.insert(b_idx, newInterval)
            return intervals

        # Merge overlapping intervals
        new_start = min(newInterval[0], intervals[b_idx][0])
        new_end = max(newInterval[1], intervals[a_idx - 1][1])

        # Remove merged section
        del intervals[b_idx:a_idx]

        # Insert merged interval
        intervals.insert(b_idx, [new_start, new_end])
        return intervals
