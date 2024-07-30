class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        result = float('inf')
        l = [[-1, -1] for _ in range(n)]
        a, b = 0, 0
        for i in range(n):
            l[i][1] = 0
            l[i][0] = b
            if s[i] == 'b':
                b += 1

        for i in range(n-1, -1, -1):
            result = min(result, l[i][0] + a)
            if s[i] == 'a':
                a += 1

        return result
