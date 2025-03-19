class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def dfs(r, c):
            if 0 > r or r >= n or 0 > c or c >= m or not grid[r][c]:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)


        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res = max(res, dfs(i, j))

        return res
