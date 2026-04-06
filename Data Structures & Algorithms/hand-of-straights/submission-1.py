class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        print(len(hand) % groupSize)
        if len(hand) % groupSize != 0:
            return False

        Ngroups = len(hand) // groupSize
        sortedHand = sorted(hand)
        mp = {}

        for h in sortedHand:
            mp[h] = mp.get(h, 0) + 1

        for group in range(Ngroups):
            # Pick smallest available value:
            for h in sortedHand:
                if mp[h]:
                    init = h
                    break
            
            for num in range(init, init + groupSize):
                if num in mp and mp[num]:
                    mp[num] -= 1
                else:
                    return False

        
        return True