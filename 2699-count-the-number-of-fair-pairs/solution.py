class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin(l, r, t):
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= t:
                    r = m-1
                else:
                    l = m+1
            return r

        nums.sort()
        res = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                bin(i+1, len(nums)-1, up+1) -
                bin(i+1, len(nums)-1, low)
            )
        return res
