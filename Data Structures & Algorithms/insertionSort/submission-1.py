# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        if pairs:
            ans.append(pairs[:]) # initial state
        for i in range(1, len(pairs)):
            for j in range(i - 1, -1, -1):
                if pairs[j].key > pairs[j+1].key:
                    temp = pairs[j]
                    pairs[j] = pairs[j+1]
                    pairs[j+1] = temp
            ans.append(pairs[:])
        return ans




        