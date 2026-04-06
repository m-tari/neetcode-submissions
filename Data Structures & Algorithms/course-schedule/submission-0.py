class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {}
        for n in prerequisites:
            if n[0] not in adj:
                adj[n[0]] = []
            adj[n[0]].append(n[1])

        def dfs(node, adj, visit):
            if node in visit:
                return False
            visit.add(node)
            if adj.get(node):
                for nei in adj[node]:
                    return dfs(nei, adj, visit)

        for node in adj:
            visit = set()
            res = dfs(node, adj, visit)
            if res is False:
                return res

        return True
        