class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in range(len(accounts)):
            print(accounts[i])
            accounts[i] = sum(accounts[i])
        return max(accounts)

