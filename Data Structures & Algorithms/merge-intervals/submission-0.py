class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key = lambda interval: interval[0])

        res = [intervals[0]]
        a_p, b_p = intervals[0]
        for a, b in intervals[1:]:
            if b_p >= a:
                res.pop()
                res.append([a_p, b])
            else:
                res.append([a, b])

            a_p, b_p = a, b

        return res