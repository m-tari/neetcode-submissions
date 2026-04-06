from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def bfs(u):
            q = deque([u])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

        res = 0
        for u in range(n):
            if u not in visit:
                bfs(u)
                res +=1

        return res