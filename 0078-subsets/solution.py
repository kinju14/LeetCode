class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(idx: int):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            dfs(idx+1)

            subset.pop()
            dfs(idx+1)

        dfs(0)
        return res
