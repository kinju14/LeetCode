class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l, res = [], []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in l:
                    res.append(grid[i][j])
                else:
                    l.append(grid[i][j])
        
        res.append(((n**2 * (n**2+1)) // 2) - sum(l))
        return res
