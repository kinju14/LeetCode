class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            dfs(idx, curr, total + candidates[idx])

            curr.pop()
            dfs(idx + 1, curr, total)

        dfs(0, [], 0)
        return res
