class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)



###########
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# Execution Tree Without Memoization:

# Starting from index 0:

# dfs(0) → tries "cat" (matches)
#   dfs(3) → tries "sand" (matches)
#     dfs(7) → tries "dog" (matches)
#       dfs(10) = True ✅
#     → returns True

# But it will also try other paths unnecessarily:

#     dfs(0) tries "cats" → dfs(4)

#         dfs(4) tries "and" → dfs(7) again!

#             If memo is not used, it reprocesses dfs(7), even though we've already seen it return True.

# The same happens for overlapping starts like:

#     dfs(3)

#     dfs(4)

#     dfs(7) (called multiple times from different paths)

# With Memoization:

# When dfs(7) is computed once, its result (True) is stored in:

# memo[7] = True

# Next time dfs(7) is needed, it's retrieved instantly:

# if 7 in memo: return memo[7]