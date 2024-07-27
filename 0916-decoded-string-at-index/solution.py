class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n, length = 0, len(s)
        
        for ch in s:
            if ch.isdigit():
                n *= int(ch)
                continue
            n += 1

        for i in range(length-1, -1, -1):
            k = k % n

            if k == 0 and s[i].isalpha():
                return s[i]

            if s[i].isdigit():
                n = n//int(s[i])

            else:
                n -= 1

            
