class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)



        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                ele = board[i][j]
                if ele in rows[i] or ele in cols[j] or ele in squares[(i//3,j//3)]:
                    return False
                
                rows[i].add(ele)
                cols[j].add(ele)
                squares[(i//3, j//3)].add(ele)

        return True





