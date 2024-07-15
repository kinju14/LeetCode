class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score = 0
        max_num = max(nums)
        for _ in range(k):
            score += max_num
            max_num += 1

        return score
