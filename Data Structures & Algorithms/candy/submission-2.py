class Solution:
    def candy(self, ratings: List[int]) -> int:
        cur = 1
        n = len(ratings)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                cur += 1
                res[i] = cur
            else:
                cur = 1
                res[i] = cur

        cur = 0
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                cur += 1
                res[i] = min(res[i] + cur, res[i+1] + 1)
            else:
                cur = 0

        return sum(res)