class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isValid(cap):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= cap:
                    i += 2
                    count += 1
                else:
                    i += 1
                
                if count == k:
                    break
            return count == k

        l, r = min(nums), max(nums)
        res = 0
        while l <= r:
            m = (l+r) // 2
            if isValid(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res

        # res = 9
        # 2 3 5 9 11
        # 2, 11 = 6
        # res = 6, l = 2, r = 5
