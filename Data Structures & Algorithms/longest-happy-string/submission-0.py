class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        self.res = []

        def dfs(a, b, c, cur):
            if len(cur) > len(self.res):
                self.res = cur.copy()
                
            if not a and not b and not c:
                return

            if cur[-2:] != ["a","a"] and a > 0:
                cur.append("a")
                dfs(a - 1, b, c, cur)
                cur.pop()

            if cur[-2:] != ["b", "b"] and b > 0:
                cur.append("b")
                dfs(a, b - 1, c, cur)
                cur.pop()

            if cur[-2:] != ["c", "c"] and c > 0:
                cur.append("c")
                dfs(a, b, c - 1, cur)
                cur.pop()


        dfs(a, b, c, [])

        return "".join(self.res)
