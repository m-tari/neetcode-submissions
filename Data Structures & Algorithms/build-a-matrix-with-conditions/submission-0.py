from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * k for _ in range(k)]

        def buildGraph(edges):
            adj = defaultdict(list)
            
            for u, v in edges:
                adj[u].append(v)
            
            return adj


        def topSort(adj):
            visit = set()
            path = set()
            res = []

            def dfs(node):
                if node in path:
                    return False

                if node in visit:
                    return True

                visit.add(node)
                path.add(node)
                for nei in adj[node]:
                    if not dfs(nei):
                        return False
                path.remove(node)
                res.append(node)
                return True
    
            for i in range(1, k + 1):
                if not dfs(i):
                    return []
            res.reverse()
            return res

        
        rowAdj = buildGraph(rowConditions)
        iList = topSort(rowAdj)
        colAdj = buildGraph(colConditions)
        jList = topSort(colAdj)

        for i, numi in enumerate(iList):
            for j, numj in enumerate(jList):
                if numi == numj:
                    matrix[i][j] = numi

        return matrix if iList and jList else []


