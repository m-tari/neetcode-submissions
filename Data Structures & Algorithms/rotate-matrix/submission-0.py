class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        matrix.reverse()

        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

# 1,1 1,2 1,3 -> 1,3 2,3 3,3
# 2,1 2,2 2,3 -> 1,2 2,2 3,2