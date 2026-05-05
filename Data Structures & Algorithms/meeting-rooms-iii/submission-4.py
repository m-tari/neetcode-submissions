import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingHeld = [0] * n 
        occupied = []  # Pair of (end, room). We hold at most n pairs in the occupied heap.
        avail = [i for i in range(n)] # Next available room (room)
        meetings.sort()

        for start, end in meetings:
            # Free occupied from all finished meetings
            while occupied and start >= occupied[0][0]:
                earliest_end ,earliest_room = heapq.heappop(occupied)
                # Now this room is available
                heapq.heappush(avail, earliest_room)

            # All rooms are booked
            if not avail:
                earliest_end ,earliest_room = heapq.heappop(occupied)
                heapq.heappush(occupied, [earliest_end + (end - start), earliest_room])
            # Get the next availabale room
            else:
                earliest_room = heapq.heappop(avail)
                heapq.heappush(occupied, [end, earliest_room])

            meetingHeld[earliest_room] += 1

        return meetingHeld.index(max(meetingHeld))