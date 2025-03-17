class Solution:
    def numberOfWays(self, s: str) -> int:
        count1, count0 = 0, 0
        count10, count01 = 0, 0
        res = 0

        for ch in s:
            if ch == '1':
                count1 +=1
                count01 += count0
                res += count10

            else:
                count0 += 1
                count10 += count1
                res += count01

        return res
