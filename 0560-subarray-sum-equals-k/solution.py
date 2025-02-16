class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {0: 1}
        result = 0
        prefixSum = 0
        for n in nums:
            prefixSum += n
            diff = prefixSum - k

            result += prefixCount.get(diff, 0)
            prefixCount[prefixSum] = 1 + prefixCount.get(prefixSum, 0)

        return result


