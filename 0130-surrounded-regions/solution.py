class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        q = deque()
        n = len(board)
        m = len(board[0])

        for i in range(n):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][m-1] == 'O':
                q.append((i, m-1))

        for j in range(m):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[n-1][j] == 'O':
                q.append((n-1, j))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            board[r][c] = '#'
            for row, col in directions:
                nr, nc = row+r, col+c
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'O':
                    q.append((nr, nc))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == '#':
                    board[i][j] = 'O'

