class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nc<0 or nc==len(grid[0]) or nr<0 or nr==len(grid) or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1
                
