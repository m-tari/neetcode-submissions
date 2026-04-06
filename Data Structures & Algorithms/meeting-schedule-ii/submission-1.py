"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        # Think of the heap as all the rooms currently in use
        heap = []

        for i in intervals:
            # Check the earliest ending room (heap[0]).
            # If the meeting starts after or at this end time, it can reuse that room → pop it from the heap.
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            # Then push the meeting’s end time into the heap (because this room is now occupied until that end).
            heapq.heappush(heap, i.end)

        # At any moment:
        # If a meeting overlaps with all existing rooms → need a new room, push into heap → heap grows.
        # If a meeting can reuse a room → pop the old end time, push the new end → heap size doesn’t grow.
        # After processing all meetings, the heap contains one end time for every room we needed at some point, 
        # which is exactly the minimum number of rooms required.
        return len(heap)


        #                                             [     ]
        #                             [          ]
        #               [    ]
        #     [                   ]
        # [                                  ]
        # 0   5  10      20           40