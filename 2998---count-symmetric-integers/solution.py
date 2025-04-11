class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for n in range(low, high + 1):
            num = str(n)
            l = len(num)
            if not l % 2:
                half = l//2
                left = sum(int(num[i]) for i in range(half))
                right = sum(int(num[i]) for i in range(half, l))

                if left == right: res += 1
        return res
                
