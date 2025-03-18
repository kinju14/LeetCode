class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        bitmask = 0
        for r in range(len(nums)):
            while bitmask & nums[r]:
                bitmask ^= nums[l]
                l += 1

            res = max(res, r-l+1)
            bitmask |= nums[r]

        return res

