from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        totalPass = defaultdict(int)
        
        for numPass, f, t in trips:
            totalPass[f] += numPass
            totalPass[t] -= numPass

        curPass = 0
        for t, p in sorted(totalPass.items()):
            curPass += p
            if curPass > capacity:
                return False

        return True
        
        # 2  3 -2 -3
        # 1  2  3  4
