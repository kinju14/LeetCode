class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(perm: str, open_count: int, close_count: int):
            if len(perm) == n*2:
                result.append(perm)
                return
            
            if open_count < n:
                backtrack(perm + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(perm + ')', open_count, close_count + 1)
            
            
        backtrack("", 0, 0)
        return result
