from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        self.hmax = 0
        self.farthest = None
        self.diam = []

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(node, h, path, visit):
            if node is None or node in visit:
                return
            
            h += 1
            visit.add(node)
            if h > self.hmax:
                self.hmax = h
                self.farthest = node
                self.diam = path.copy()

            for nei in adj[node]:
                path.append(nei)
                dfs(nei, h, path, visit)
                path.pop()

            return

        dfs(0, 0, [], set())
        V1 = self.farthest
        
        self.hmax = 0
        dfs(V1, 0, [V1], set())
        
        l = len(self.diam)
        if l % 2 == 0:
            return [self.diam[l // 2], self.diam[l // 2 - 1]]
        else:
            return [self.diam[l // 2]]
