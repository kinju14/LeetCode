class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, subset, currSum):
            if currSum == target:
                res.append(subset.copy())
                return

            if currSum > target or idx >= len(candidates):
                return

            subset.append(candidates[idx])
            backtrack(idx+1, subset, currSum + candidates[idx])
            subset.pop()

            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1

            backtrack(idx+1, subset, currSum)

        backtrack(0, [], 0)
        return res

        
