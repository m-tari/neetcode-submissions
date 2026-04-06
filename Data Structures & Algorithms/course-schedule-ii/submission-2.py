class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        order = []
        visit = set()
        path = set()
        for i in range(numCourses):
            if not self.dfs(i, adj, order, visit, path):
                return []

        return order

    def dfs(self, i, adj, order, visit, path):
        if i in path:
            return False
        if i in visit:
            return True
        visit.add(i)
        path.add(i)
        for nei in adj[i]:
            if not self.dfs(nei, adj, order, visit, path):
                return False
        path.remove(i)
        order.append(i)

        return True