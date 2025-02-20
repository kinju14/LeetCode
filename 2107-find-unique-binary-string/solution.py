class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)

        def backtrack(s: str) -> str:
            if len(s) == len(nums):
                return s

            for i in range(2):
                st = backtrack(s + str(i))
                if st not in nums:
                    return st
            
            return st

        return backtrack('')
