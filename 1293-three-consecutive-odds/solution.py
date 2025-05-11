class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0

        for r in arr:
            c = c + 1 if r % 2 != 0 else 0
            if c == 3:
                return True

        return False
