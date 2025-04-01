class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]

            if i >= len(questions):
                return 0
            
            p, n = questions[i]
            dp[i] = max(p + dfs(i+1+n), dfs(i+1))
            return dp[i]

        return dfs(0)
