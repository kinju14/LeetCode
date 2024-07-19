class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        d = {}

        for i in range(n):
            d[i] = min(matrix[i])
            k = matrix[i].index(d[i])
            # print(d, k)
            for j in range(n):
                if matrix[j][k] > d[i]:
                    del d[i]
                    # print(d)
                    break
        # print(d)

        return d.values()

