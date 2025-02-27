class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        rows, cols = len(matrix)-1, len(matrix[0])-1

        for i in range(rows+1):
            if matrix[i][0] <= target and target <= matrix[i][cols]:
                l, r = 0, cols
                while l <= r:
                    m = (l+r) // 2
                    print(l, r, i, m)
                    if matrix[i][m] == target:
                        found = True
                        break
                    if target < matrix[i][m]:
                        r = m-1
                    else:
                        l = m+1
                if found: 
                    break

        return found
