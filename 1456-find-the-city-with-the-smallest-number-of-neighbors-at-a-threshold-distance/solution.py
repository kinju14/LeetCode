class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for x in range(n):
            matrix[x][x] = 0 
        
        for [n1, n2, w] in edges:
            matrix[n1][n2] = w
            matrix[n2][n1] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    num = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    matrix[i][j] = num

        city = -1
        c = n
        for i in range(n):
            count = 0
            for j in range(n):
                if matrix[i][j] <= distanceThreshold: count += 1
            
            if count <= c:
                c = count
                city = i
            
        return city


