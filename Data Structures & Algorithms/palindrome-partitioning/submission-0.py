class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def backtrack(i, j, cur):
            if i == n:
                res.append(cur[:])
                return
            
            if j == n:
                return

            if s[i: j + 1] == s[i: j + 1][:: -1]:
                cur.append(s[i: j + 1])

                backtrack(j + 1, j + 1, cur)
                cur.pop()

            backtrack(i, j + 1, cur)


        backtrack(0, 0, [])
        return res

#                 ij
#        s = "abc"