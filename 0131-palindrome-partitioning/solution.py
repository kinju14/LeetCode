class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(i: int, currList: list):
            if i >= len(s):
                res.append(currList[:])
                return

            for j in range(i+1, len(s)+1):
                if isPalindrome(s[i:j]):
                    backtrack(j, currList + [s[i:j]])


        backtrack(0, [])
        return res
