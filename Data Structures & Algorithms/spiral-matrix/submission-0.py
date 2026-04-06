class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        l, t, r, b = 0, 0, n - 1, m - 1

        k = 0
        while k != m * n:
            for j in range(l, r + 1):
                res.append(matrix[t][j])
                k += 1
            t += 1

            for i in range(t, b + 1):
                res.append(matrix[i][r])
                k += 1
            r -= 1

            if t <= b:
                for j in range(r, l - 1, -1):
                    res.append(matrix[b][j])
                    k += 1
                b -= 1

            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                    k += 1
                l += 1

        return res