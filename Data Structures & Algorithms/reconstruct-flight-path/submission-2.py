from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        n = len(tickets)

        for u, v in tickets:
            adj[u].append(v)

        res = ["JFK"]

        def dfs(node):
            if len(res) == n + 1:
                return True
            
            for i, nei in enumerate(adj[node]):
                    adj[node].pop(i)
                    res.append(nei)
                    if dfs(nei): 
                        return True
                    adj[node].insert(i, nei)
                    res.pop()
            
            return False

        dfs("JFK")

        return res