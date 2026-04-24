from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for src, dst in trust:
            outdegree[src] += 1
            indegree[dst] += 1

        for node in range(1, n + 1):
            if indegree[node] == n - 1 and outdegree[node] == 0:
                return node

        return -1
