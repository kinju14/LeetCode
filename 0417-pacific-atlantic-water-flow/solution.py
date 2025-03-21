class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        n, m = len(heights), len(heights[0])
        atlantic_set = set()
        pacific_set = set()

        def dfs(r, c, visited_set, preVal):
            if (r, c) in visited_set or r >= n or r < 0 or c >= m or c < 0 or \
            heights[r][c] < preVal:
                return

            visited_set.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited_set, heights[r][c])
        
        for r in range(n):
            dfs(r, 0, pacific_set, heights[r][0])
            dfs(r, m-1, atlantic_set, heights[r][m-1])

        for c in range(m):
            dfs(0, c, pacific_set, heights[0][c])
            dfs(n-1, c, atlantic_set, heights[n-1][c])

        return list(pacific_set & atlantic_set)
