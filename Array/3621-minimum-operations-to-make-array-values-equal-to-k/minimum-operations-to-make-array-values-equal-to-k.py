class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for n in nums:
            if n < k:
                return -1
        res = 0
        nums = set(nums)
        for n in nums:
            if n > k:
                res += 1
        return res


