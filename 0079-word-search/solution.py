class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def backtrack(wPt: int, idx: int, jdx: int):
            if wPt == len(word):
                return True

            if idx < 0 or idx >= n or jdx < 0 or jdx >= m or board[idx][jdx] != word[wPt]:
                return False
            
            temp = board[idx][jdx]
            board[idx][jdx] = '#'

            found = (backtrack(wPt+1, idx+1, jdx) or 
                    backtrack(wPt+1, idx-1, jdx) or 
                    backtrack(wPt+1, idx, jdx+1) or  
                    backtrack(wPt+1, idx, jdx-1))

            board[idx][jdx] = temp

            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and backtrack(0, i, j):
                    return True

        return False
