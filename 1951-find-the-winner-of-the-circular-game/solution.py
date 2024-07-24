
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [x for x in range(1, n+1)]
        c = n -1
        i = 0
        while c > 0:
            i -= 1
            i = (i + k) % len(l)
            l.pop(i)
            c -= 1

        return l[0]
