import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Use heap to track active passengers in the car and who is getting off next
        # Sort trips basesd on start time
        # For each trip:
        # Drop off all passengers who have a drop off less than end of the trip
        # Pick up passengers of current trip
        # Check if the capacity limit is maintained

        trips.sort(key = lambda trip: trip[1])
        heap = []  # [end, numPass]
        curPass = 0

        for numPass, start, end in trips:
            while heap and heap[0][0] <= start:
                curPass -= heapq.heappop(heap)[1]

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(heap, [end, numPass])

        return True

        
        # 2  3 -2 -3
        # 1  2  3  4
