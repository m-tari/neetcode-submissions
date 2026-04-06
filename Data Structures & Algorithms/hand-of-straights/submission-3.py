from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        cnt = Counter(hand)

        for h in hand:
            if cnt[h]:
                for num in range(h, h + groupSize):
                    if num in cnt and cnt[num]:
                        cnt[num] -= 1
                    else:
                        return False

        return True