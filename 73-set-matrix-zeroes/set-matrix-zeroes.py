class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        def mark_infinity(matrix, row, col):
            for i in range(r):
                if matrix[i][col] != 0:
                    matrix[i][col] = float("inf")
            for j in range(c):
                if matrix[row][j] != 0:
                    matrix[row][j] = float("inf")

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    mark_infinity(matrix, i, j)

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
