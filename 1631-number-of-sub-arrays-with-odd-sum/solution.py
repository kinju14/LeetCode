class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        currSum, odd, even, result = 0, 0, 0, 0

        for n in arr:
            currSum += n

            if currSum % 2:
                result += 1 + even
                odd += 1
            else:
                result += odd
                even += 1

        return result % (10**9+7)
