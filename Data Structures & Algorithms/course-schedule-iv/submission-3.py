from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] = prereqMap[crs] | dfs(prereq) # Union of direct and indirect prerequisites
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {} # crs -> set of all direct and indirect prerequisites
        for i in range (numCourses):
            dfs(i)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])

        return res


