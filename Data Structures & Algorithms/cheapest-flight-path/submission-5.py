from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        q = deque([src])
        adj = defaultdict(list)

        for u, v, p in flights:
            adj[u].append((v, p))

        l = 0
        t = [float("inf")] * n  # total price from src to each node
        t[src] = 0

        while q and  l < k + 1:
            temp = t[:]
            for i in range(len(q)):
                node = q.popleft()
                if node == dst:
                    continue
                for nei, p in adj[node]:
                    q.append(nei)
                    temp[nei] = min(p + t[node], t[nei])
            t = temp
            l += 1
            
        return t[dst] if t[dst] != float("inf") else -1