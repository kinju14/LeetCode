class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4 : return 0
        n = len(nums)
        d = dict()
        result = 0
        for i in range(n-1):
            for j in range(i+1, n):
                val = nums[i] * nums[j]
                if val in d:
                    result += d[val]*8
                    d[val] += 1
                else:
                    d[val] = 1

        return result
