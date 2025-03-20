class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStr = ''
        resLen = 0
        def check(l, r):
            nonlocal resLen, resStr
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resStr = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

        for i in range(len(s)):
            check(i, i)
            check(i, i+1)

        return resStr

