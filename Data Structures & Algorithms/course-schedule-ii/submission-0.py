class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        order = []
        visit = set()
        for i in range(numCourses):
            path = set()
            res = self.dfs(i, adj, order, visit, path)
            if not res:
                return []

        return order

    def dfs(self, i, adj, order, visit, path):
        if i in path:
            return False
        if i in visit:
            return True
        visit.add(i)
        path.add(i)
        res = True
        for nei in adj[i]:
            res = self.dfs(nei, adj, order, visit, path)
        order.append(i)

        return res