class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for n in range(1, amount+1):
            for c in coins:
                if n-c >= 0:
                    dp[n] = min(dp[n], 1 + dp[n - c])
        
        return dp[amount] if dp[amount] != amount+1 else -1

        '''
        dp = {}
        def dfs(amt):
            if amt in dp:
                return dp[amt]

            if not amt:
                return 0
            
            if amt < 0:
                return float('inf')

            minCoins = float('inf')
            for c in coins:
                res = dfs(amt - c)
                if res != float('inf'):
                    minCoins = min(minCoins, res+1)

            dp[amt] = minCoins

            return minCoins

        res = dfs(amount)
        return res if res != float('inf') else -1
        '''
