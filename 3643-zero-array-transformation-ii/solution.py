class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l, r = 0, len(queries)
        k = -1

        def valid(ans):
            diffArr = [0 for _ in range(len(nums)+1)]

            for l, r, val in queries[:ans]:
                diffArr[l] += val
                diffArr[r+1] -= val

            for i in range(1, len(diffArr)):
                diffArr[i] += diffArr[i-1]

            for i in range(len(nums)):
                if nums[i] > diffArr[i]:
                    return False
            return True
        
        
        while l <= r:
            mid = (l+r) // 2
            if valid(mid):
                k = mid
                r = mid -1
            else:
                l = mid + 1

        return k

        
