from collections import defaultdict

class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        cur = node
        while self.par[cur] != cur:
            cur = self.par[self.par[cur]]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] > self.size[pv]:
            pu, pv = pv, pu
        self.par[pv] = pu
        self.size[pu] += self.size[pv]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Step 1
        # Create a list of unqiue emails with idx of acc and union the already seen email to merge acc
        emailsToAcc = {}  # email -> idx of acc
        # Step 2
        # Go through all unique emails and group them with the leader (root parent) of that group unsing uf.find
        emailGroup = defaultdict(list)  # idx of acc -> list of email


        uf = UF(len(accounts))
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e in emailsToAcc:
                    uf.union(i, emailsToAcc[e])
                else:
                    emailsToAcc[e] = i

        for e, i in emailsToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i, group in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + group)

        return res