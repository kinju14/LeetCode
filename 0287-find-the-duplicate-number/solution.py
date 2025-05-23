class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Algo: 2 phases of slow and fast pointers

        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s
