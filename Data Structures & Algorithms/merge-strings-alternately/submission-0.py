class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ""
        n, m = len(word1), len(word2)
        i, j = 0, 0

        while i < n and j < m:
            res += word1[i] + word2[j]
            i += 1
            j += 1

        if i < n:
            for k in range(i, n):
                res += word1[k]

        if j < m:
            for k in range(j, m):
                res += word2[k]

        return res