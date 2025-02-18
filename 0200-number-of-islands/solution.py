class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0

        #DFS
        def dfs(r, c):
            if 0 > r or r >= n or 0 > c or c >= m or grid[r][c] == '0':
                return

            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # BFS
        '''
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(r, c):
            queue = deque([(r,c)])
            grid[r][c] = 0

            while queue:
                [row, col] = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
        '''

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    result += 1
                    #bfs(i, j)
                    dfs(i,j)

        return result
