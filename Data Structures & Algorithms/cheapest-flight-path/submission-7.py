from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        costs = [float("inf")] * n  # total price from src to each node
        costs[src] = 0

        for _ in range(k + 1):
            temp = costs[:]
            for s, d, p in flights:
                if costs[s] + p < temp[d]:
                    temp[d] = costs[s] + p
            costs = temp
            
        return costs[dst] if costs[dst] != float("inf") else -1