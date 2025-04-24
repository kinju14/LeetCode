class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        res = 0
        n = len(nums)

        for i in range(n):
            curr = set()
            for j in range(i, n):
                curr.add(nums[j])
                if len(curr) == distinct:
                    res += (n-j)
                    break
        return res


