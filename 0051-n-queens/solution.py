class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)]for _ in range(n)]

        def canPlace(r, c, board):
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
                
            for j in range(c):
                if board[r][j] == 'Q':
                    return False
            
            i = r-1
            j = c-1
            while i >=0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = r+1
            j = c-1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True
        
        res = []

        def backtrack(c):
            if c == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for r in range(n):
                if canPlace(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(c+1)
                    board[r][c] = '.'

        backtrack(0)
        return res
