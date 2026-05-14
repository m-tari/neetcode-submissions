from math import gcd
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        adj = defaultdict(list)

        # Create the graph wtih gcd
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(nums[i], nums[j]) > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        # See if the graph is connected
        visit = set()
        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(0)

        return len(visit) == n

        # [4, 3, 12]
        #  4   -   12    -  3