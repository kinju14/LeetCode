class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        answer = [0] * len(queries)
        n, m = len(grid), len(grid[0])
        indexes = sorted(range(len(queries)), key = lambda x: queries[x])

        minHeap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        total = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for idx in indexes:
            while minHeap and minHeap[0][0] < queries[idx]:
                val, i, j = heappop(minHeap)
                total += 1
                for r, c in directions:
                    nr, nc = r + i, c + j
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                        heappush(minHeap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))

            answer[idx] = total
        return answer

