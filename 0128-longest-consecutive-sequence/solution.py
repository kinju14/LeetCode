class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        maxLen = 0
        for n in nums:
            if n-1 not in nums:
                length = 1
                while n+1 in nums:
                    length += 1
                    n = n+1
                maxLen = max(maxLen, length)
        return maxLen
