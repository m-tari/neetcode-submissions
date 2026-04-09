from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Step 1
        # Create a graph where emails are nodes and all emails in an account are connected  (star-like to first email)
        # Step 2
        # Go through all emails and find connected components using DFS

        adj = defaultdict(list)
        for i, acc in enumerate(accounts):
            first_email = acc[1]
            # Ensure the first email is always a key (If an account has only one email)
            if first_email not in adj:
                adj[first_email] = []
            for e in acc[2:]:
                adj[first_email].append(e)
                adj[e].append(first_email)

        visit = set()
        res = []

        def dfs(node, comp):
            visit.add(node)
            comp.append(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei, comp)

        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e not in visit:
                    component = []
                    dfs(e, component)
                    name = acc[0]
                    res.append([name]+ sorted(component))

        return res
        
