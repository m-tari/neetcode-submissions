from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = defaultdict(int)
        
        for numPass, start, end in trips:
            locations[start] += numPass
            locations[end] -= numPass

        curPass = 0
        for t, p in sorted(locations.items()):
            curPass += p
            if curPass > capacity:
                return False

        return True
        
        # 2  3 -2 -3
        # 1  2  3  4
