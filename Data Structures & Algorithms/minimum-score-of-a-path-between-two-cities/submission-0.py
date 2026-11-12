from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        score = float("inf")

        for src, dst, dist in roads:
            adj[src].append([dst, dist])
            adj[dst].append([src, dist])

        q = deque([1])
        visited = set()

        while q:
            node = q.popleft()
        
            for nei, d in adj[node]:
                score = min(d, score)
                
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return score