class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diffArr = [0 for _ in range(len(nums)+1)]

        for l, r in queries:
            diffArr[l] += 1
            diffArr[r+1] -= 1

        for i in range(1, len(diffArr)):
            diffArr[i] += diffArr[i-1]

        for i in range(len(nums)):
            if nums[i] > diffArr[i]:
                return False
        return True



