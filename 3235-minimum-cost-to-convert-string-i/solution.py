class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        uniqueChars = set(source).union(set(target)).union(set(original)).union(set(changed))
        n = len(uniqueChars)
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        d = {k: v for v, k in enumerate(uniqueChars)}

        n = len(original)
        for i in range(n):
            if matrix[d[original[i]]][d[changed[i]]] > cost[i]: 
                matrix[d[original[i]]][d[changed[i]]] = cost[i]

        n = len(d)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    num = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    matrix[i][j] = num

        n = len(source)
        result = 0
        for i, j in zip(source, target):
            if i != j:
                result += matrix[d[i]][d[j]]

        if result == float('inf'): 
            return -1
        return result

