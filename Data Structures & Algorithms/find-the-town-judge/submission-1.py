from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(set)

        for u, v in trust:
            adj[u].add(v)

        # Find a node with out-degree of zero 
        cnt = 0
        candidate = None
        for node in range(1, n + 1):
            if node not in adj:
                candidate = node
                cnt += 1
            # There must be exactly one person as a judge
            if cnt > 1:
                return -1

        if not candidate:
            return -1

        # Check if the out-degree of candidate is  n - 1
        out_deg = 0
        for node, neis in adj.items():
            if node != candidate and candidate in neis:
                out_deg += 1

        return candidate if out_deg == n - 1 else -1
