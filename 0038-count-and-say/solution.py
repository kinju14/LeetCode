class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        res = ''

        prev = self.countAndSay(n-1)
        i = 0

        while i < len(prev):
            currCount = 1
            while i+1 < len(prev) and prev[i] == prev[i+1]:
                currCount += 1
                i += 1
            res += str(currCount) + prev[i]
            i += 1
        return res
