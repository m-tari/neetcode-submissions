from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        visit = set()
        path = set()
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)

        def dfs(node):
            if node in path:
                return True

            if node in visit:
                return False

            path.add(node)
            visit.add(node)
            for nei in adj[node]:
                if dfs(nei):
                    return True

            path.remove(node)
            res.append(node)
            return False

        for i in range(n):
            if dfs(i):
                return []

        res.reverse()
        return res


