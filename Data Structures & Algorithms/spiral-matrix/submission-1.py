class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        l, t, r, b = 0, 0, n - 1, m - 1

        while t <= b and l <= r:
            for j in range(l, r + 1):
                res.append(matrix[t][j])
            t += 1

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            if not (t <= b and l <= r):
                break

            for j in range(r, l - 1, -1):
                res.append(matrix[b][j])
            b -= 1

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res