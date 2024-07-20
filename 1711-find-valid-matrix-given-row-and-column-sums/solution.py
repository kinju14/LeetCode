class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        nRow, nCol = len(rowSum), len(colSum)
        matrix = [[-1 for _ in range(nCol)] for _ in range(nRow)]

        for i in range(nRow):
            for j in range(nCol):
                x = min(rowSum[i], colSum[j])
                matrix[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x

        return matrix






