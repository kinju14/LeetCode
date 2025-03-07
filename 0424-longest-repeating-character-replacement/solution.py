class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = {}
        result = 0
        l, r = 0, 0

        while r < len(s):
            countChar[s[r]] = 1 + countChar.get(s[r], 0)
            if (r-l+1) - max(countChar.values()) > k:
                countChar[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
            r += 1
        
        return result
