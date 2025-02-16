class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        zero, one = 0, 0
        d = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            
            if one-zero not in d:
                d[one-zero] = i
            
            if one == zero:
                result = one + zero
            else:
                idx = d[one-zero]
                result = max(result, i-idx)
        return result

