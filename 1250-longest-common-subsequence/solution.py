class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]

                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
        # memo = {}
        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     if text1[i] == text2[j]:
        #         memo[(i, j)] = 1 + dfs(i+1, j+1)

        #     else:
        #         memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            
        #     return memo[(i, j)]

        # return dfs(0, 0)
        
