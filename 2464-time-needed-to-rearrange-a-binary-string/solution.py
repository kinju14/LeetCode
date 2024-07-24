class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        c = 0

        while s.count('01') > 0:
            s = s.replace('01','10')
            c += 1
        
        return c
