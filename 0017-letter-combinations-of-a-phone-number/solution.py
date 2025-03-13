class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToCharMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
                        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        def backtrack(idx, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            for ch in numToCharMap[digits[idx]]:
                backtrack(idx+1, currStr + ch)

        if digits:
            backtrack(0, '')

        return res
        
