class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            res += 1

        return res
            