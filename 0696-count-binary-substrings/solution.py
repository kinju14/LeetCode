class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        
        if len(s) == 1:
            return result

        n = len(s)
        prevLen, currLen = 0, 1

        for i in range(1,n):
            if s[i] == s[i-1]:
                currLen += 1

            else:
                prevLen = currLen
                currLen = 1

            if prevLen >= currLen:
                result += 1

        return result


            

