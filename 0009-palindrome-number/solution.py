class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        total = 0
        n = x
        while n > 0:
            total = (total * 10 ) + (n%10)
            n = n//10

        return total == x
