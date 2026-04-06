class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        b_idx = 0
        a_idx = len(intervals) - 1
        for idx, intvl in enumerate(intervals):
            if intvl[0] < newInterval[0]:
                b_idx = idx
            if intvl[1] > newInterval[1]:
                a_idx = min(idx, a_idx)

        # no merge
        if intervals[b_idx][1] < newInterval[0] and intervals[a_idx][0] > newInterval[1]:
            intervals.insert(b_idx + 1, newInterval)
            return intervals

        s_pop, e_pop = b_idx, a_idx + 1 # not include
        # merge
        if intervals[b_idx][1] > newInterval[0]:
            newInterval[0] = min(intervals[b_idx][0], newInterval[0])
        if intervals[a_idx][0] < newInterval[1]:
            newInterval[1] = max(intervals[a_idx][1], newInterval[1])

        del intervals[s_pop:e_pop]

        intervals.insert(s_pop, newInterval)
        return intervals

