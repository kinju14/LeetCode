class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        def helper(arr):
            prev, curr = 0, 0
            for n in arr:
                temp = max(n+prev, curr)
                prev = curr
                curr = temp

            return curr
            
        return max(helper(nums[:-1]), helper(nums[1:]))
