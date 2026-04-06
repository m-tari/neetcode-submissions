from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        costs = [float("inf")] * n  # total price from src to each node
        costs[src] = 0

        # Bellman Ford Algorithm
        for _ in range(k + 1):
            # We use a temporary array each iteration so that paths from the same iteration 
            # don't chain together and accidentally exceed the allowed number of flights.
            # Example to prove it's needed:
            # n = 4
            # flights = [
            # [0,1,100],
            # [0,2,500],
            # [1,2,100],
            # [2,3,100]
            # ]
            # src = 0
            # dst = 3
            # k = 1
            temp = costs[:]
            for s, d, p in flights:
                if costs[s] + p < temp[d]:
                    temp[d] = costs[s] + p
            costs = temp
            
        return costs[dst] if costs[dst] != float("inf") else -1