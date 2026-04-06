# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def _quickSortHelper(self, pairs: List[Pair], s: int, e: int):
        if s >= e:
            return

        pivot = pairs[e]
        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1

        pairs[e], pairs[left] = pairs[left], pairs[e]

        self._quickSortHelper(pairs, s, left - 1)
        self._quickSortHelper(pairs, left + 1, e)


# Why not slicing instead of s, e indices?
# self.quickSort(pairs[:left])
# self.quickSort(pairs[left:])

# Slicing pairs like this creates new sublists, but you're not modifying 
#the original list in-place, so the recursion does not affect the original pairs.

# ✅ Fix: Perform recursive calls with start and end indices, and sort in-place.
        