class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A valid tree has exactly n - 1 edges

        visit = set()
        adj = {}

        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True


        return dfs(0, -1) and len(visit) == n  # no disconnected components
        