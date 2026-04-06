class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(word1):
                return len(word2[j:])

            if j>= len(word2):
                return len(word1[i:])
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            #  Delete
            delete = dfs(i + 1, j) + 1
            # Replace
            replace = dfs(i + 1, j + 1) + 1
            # Insert
            insert = dfs(i, j + 1) + 1

            op = min(delete, replace, insert)

            cache[(i, j)] = op

            return op

        return dfs(0, 0)
