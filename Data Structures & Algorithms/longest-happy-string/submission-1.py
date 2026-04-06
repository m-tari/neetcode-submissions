class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        count = [[a, "a"], [b, "b"], [c, "c"]]

        while True:
            count.sort()
            if res[-2:] != count[-1][1] * 2 and count[-1][0] > 0:
                res += count[-1][1]
                count[-1][0] -= 1
            elif res[-2:] != count[-2][1] * 2 and count[-2][0] > 0:
                res += count[-2][1]
                count[-2][0] -= 1
            elif res[-2:] != count[-3][1] * 2 and count[-3][0] > 0:
                res += count[-3][1]
                count[-3][0] -= 1
            else:
                return res