class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def stockTrade(i, canBuy):
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if i >= len(prices):
                return 0

            if canBuy:
                memo[(i, canBuy)] = max(stockTrade(i+1, False) - prices[i], stockTrade(i+1, True))
            else:
                memo[(i, canBuy)] = max(stockTrade(i+2, True) + prices[i], stockTrade(i+1, False))

            return memo[(i, canBuy)]
            
        return stockTrade(0, True)
