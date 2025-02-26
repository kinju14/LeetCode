class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currSum, maxSum = 0, 0
        minSum = 0
        result = 0

        for n in nums:
            currSum += n
            result = max(result, abs(currSum-maxSum), abs(currSum-minSum))
            maxSum = max(maxSum, currSum)
            minSum = min(currSum, minSum)

        return result
