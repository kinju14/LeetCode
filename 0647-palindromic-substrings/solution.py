class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def countPalin(l, r):
            nonlocal res
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            #odd len
            countPalin(i, i)
            countPalin(i, i+1)

        return res
