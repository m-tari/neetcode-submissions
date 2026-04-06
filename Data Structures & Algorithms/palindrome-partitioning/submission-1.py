class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def backtrack(i, cur):            
            if i == n:
                res.append(cur[:])
                return

            for j in range(i + 1, n + 1):
                if s[i: j] == s[i: j][:: -1]:
                    cur.append(s[i: j])
                    backtrack(j, cur)
                    cur.pop()

        backtrack(0, [])
        return res

#                 ij
#        s = "abc"