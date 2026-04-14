class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)

        for i in range(1, n):
            a = words[i-1]
            b = words[i]
            j, k = 0, 0

            while j < len(a) and k < len(b):
                if order.index(a[j]) > order.index(b[k]):
                    return False
                elif order.index(a[j]) == order.index(b[k]):
                    j += 1
                    k += 1
                else:
                    break

            # If we compared all character in two consecutive words and they are the same,
            # The shorter must appear before longer, otherwise it's not correctly ordered.
            if j < len(a) and k == len(b):
                return False

        return True 