"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        timeMeetingMap = defaultdict(int)
        for i in intervals:
            timeMeetingMap[i.start] += 1
            timeMeetingMap[i.end] -= 1

        cur =0
        res = 0
        for i in sorted(timeMeetingMap.keys()):
            cur += timeMeetingMap[i]
            res = max(res, cur)

        return res
        #                                             [     ]
        #                             [          ]
        #               [    ]
        #     [                  ]
        # [                                  ]
        # 0   5  10      20           40