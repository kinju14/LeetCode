class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(2, len(nums)):
            if not nums[i-2]:
                nums[i-2] = not nums[i-2]
                nums[i-1] = not nums[i-1]
                nums[i] = not nums[i]
                res += 1

        if nums[-2] and nums[-1]:
            return res
        return -1

