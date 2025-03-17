class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        posLen = 0
        negLen = 0
        maxLen = 0
        for n in nums:
            if n > 0:
                posLen += 1
                negLen += 1 if negLen else 0
            elif n < 0:
                prev = True if negLen else False
                posLen, negLen = negLen, posLen
                negLen += 1
                posLen += 1 if prev else 0
            maxLen = max(maxLen, posLen)
            if n == 0:
                posLen, negLen = 0, 0
        
        return maxLen
        

