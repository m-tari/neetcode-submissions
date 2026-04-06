from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        n = len(tickets)

        for u, v in tickets:
            adj[u].append(v)

        visit = set()  # Stores visited edges
        topSort = []

        def dfs(node):
            
            for nei in sorted(adj[node]):
                if (node, nei) not in visit:
                    visit.add((node, nei))
                    dfs(nei)

            topSort.append(node)

        dfs("JFK")

        topSort.reverse()

        return topSort