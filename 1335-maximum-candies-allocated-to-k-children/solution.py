class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        r = sum(candies)
        if r < k:
            return 0

        l = 1
        def canDivide(m):
            total = 0
            for i in range(len(candies)):
                total += (candies[i] // m)
            return total >= k           

        while l <= r:
            mid = (l+r) // 2
            if canDivide(mid):
                l = mid+1
            else:   
                r = mid-1

        return r

