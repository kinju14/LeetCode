class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        res = s[:2]

        for i in range(2, len(s)):
            if res[-1] == s[i] and s[i] == res[-2]:
                continue
            res += s[i]
        return res

