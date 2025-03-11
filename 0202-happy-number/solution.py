class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumSq(num: int) -> int:
            total = 0
            while num > 0:
                total += (num%10)**2
                num //= 10
            return total
        
        while True:
            n = sumSq(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)

