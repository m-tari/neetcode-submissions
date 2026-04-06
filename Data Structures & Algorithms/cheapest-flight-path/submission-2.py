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
        for i in range(n):
            t[i] = float("inf")
        
        t[src] = 0
        while q and  l < k + 1:
            for i in range(len(q)):
                node = q.popleft()
                if node == dst:
                    break
                for nei, p in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                        t[nei] = min(p + t[node], t[nei])
            l += 1
            
        return t[dst] if t[dst] != float("inf") else -1