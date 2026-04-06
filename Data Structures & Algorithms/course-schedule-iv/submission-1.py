class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        

        def dfs(src, adj, topSort, visit):
            if src in visit:
                return

            visit.add(src)

            for n in adj[src]:
                dfs(n, adj, topSort, visit)
            topSort.append(src)


        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for src, dst in prerequisites:
            adj[src].append(dst)

        topSort = []
        visit = set()

        for i in range(numCourses):
            dfs(i, adj, topSort, visit)

        topSort.reverse()

        res = []
        for u, v in queries:
            try:
                uIndex = topSort.index(u)
                vIndex = topSort.index(v)
            except:
                res.append(False)
                continue

            if uIndex < vIndex:
                res.append(True)
            else:
                res.append(False)

        return res

