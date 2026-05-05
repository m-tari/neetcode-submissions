import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingHeld = [0] * n 
        occupied = []  # pair of (end, room)
        avail = [i for i in range(n)] # next available room (room)
        meetings.sort()

        for start, end in meetings:
            while occupied and start >= occupied[0][0]:
                earliest_end ,earliest_room = heapq.heappop(occupied)
                heapq.heappush(avail, earliest_room)

            # all rooms are booked
            if len(occupied) >= n:
                earliest_end ,earliest_room = heapq.heappop(occupied)
                heapq.heappush(occupied, [earliest_end + (end - start), earliest_room])
                meetingHeld[earliest_room] += 1
                continue

            # Get next availabale room
            n_room = heapq.heappop(avail)
            heapq.heappush(occupied, [end, n_room])
            meetingHeld[n_room] += 1

        res = meetingHeld.index(max(meetingHeld))
        return res