class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d=1
        i=1
        while (time>0):
            i+=d
            if (i%n == 0 or i == 1):
                d = d * -1
            time-=1
        return i
