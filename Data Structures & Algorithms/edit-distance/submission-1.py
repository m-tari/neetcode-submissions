class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def dfs(i, j):
            if i >= len(word1):
                return len(word2[j:])

            if j>= len(word2):
                return len(word1[i:])
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            #  Delete
            d = dfs(i + 1, j) + 1
            # Replace
            r = dfs(i + 1, j + 1) + 1
            # Insert
            i = dfs(i, j + 1) + 1

            op = min(d, r, i)

            return op

        return dfs(0, 0)
