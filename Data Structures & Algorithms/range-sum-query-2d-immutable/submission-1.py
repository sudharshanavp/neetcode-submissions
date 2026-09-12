class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            prefix = 0
            for j in range(cols):
                prefix += matrix[i][j]
                self.sum_matrix[i+1][j+1] = self.sum_matrix[i][j+1] + prefix
        print(self.sum_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        sub_matrix = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1-1][col2]
        top_left = self.sum_matrix[row2][col1-1]
        top_left_corner = self.sum_matrix[row1 - 1][col1 - 1]
        return sub_matrix - above - top_left + top_left_corner


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)