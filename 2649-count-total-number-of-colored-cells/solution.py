class Solution:
    def coloredCells(self, n: int) -> int:
        # res = 1
        
        # while n > 1:
        #     temp = 4 * (n-1)
        #     res += temp
        #     n -= 1

        # return res

        return 2*n*(n-1)+1
