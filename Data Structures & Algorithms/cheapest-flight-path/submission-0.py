from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        visit = set()
        q = deque([src])
        adj = defaultdict(list)

        for u, v, p in flights:
            adj[u].append((v, p))

        l = 0
        t = {}  # total price from src to each node
        t[src], t[dst] = 0,  0 
        while q and  l < k + 1:
            for i in range(len(q)):
                node = q.popleft()
                if node == dst:
                    return t[node]
                for nei, p in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                        t[nei] = p + t[node]
            l += 1
            
        return t[dst] if t[dst] else -1