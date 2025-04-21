class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = lower
        mini, maxi = lower, lower

        for i in range(1, len(differences) + 1):
            curr = differences[i-1] + prev
            mini = min(mini, curr)
            maxi = max(maxi, curr)
            prev = curr

        res = (upper - lower + 1) - (maxi - mini)
        return res if res > 0 else 0

        


