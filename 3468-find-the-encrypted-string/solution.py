class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        if n == k:
            return s
        k = k % n
        return s[k:] + s[:k]


