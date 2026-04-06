from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        n = len(tickets)

        for u, v in tickets:
            adj[u].append(v)

        res = []

        def dfs(node):
            while adj[node]:
                    nei = adj[node].pop()
                    dfs(nei)

            res.append(node)

        dfs("JFK")

        res.reverse()
        return res