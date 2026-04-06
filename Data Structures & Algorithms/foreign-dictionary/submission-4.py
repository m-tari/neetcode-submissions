from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c: [] for w in words for c in w}
        n = len(words)
        for i in range(1, n):
            pre = words[i - 1]
            cur = words[i]
            if len(pre) > len(cur) and pre.startswith(cur):
                return ""
            minL = min(len(pre), len(cur))
            for j in range(minL):
                if pre[j] != cur[j]:
                    adj[pre[j]].append(cur[j])
                    break

        topSort = []
        visit = set()
        # We use a hashset for cycle detection since acyclical graph is not guaranteed in the constraints.
        # If we find a cycle, we immediatly return True, and the words list order is invalid.
        path = set()

        def dfs(node):
            if node in path:
                return True
            if node in visit:
                return False

            visit.add(node)
            path.add(node)

            for nei in adj[node]:
                if dfs(nei):
                    return True

            topSort.append(node)
            path.remove(node)
            return False

        for node in adj:
            if dfs(node):
                return ""

        topSort.reverse()
        return "".join(topSort)
