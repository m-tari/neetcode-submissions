class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False

        l = 0
        r = cols - 1

        while r >= l:
            m = (r + l) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False