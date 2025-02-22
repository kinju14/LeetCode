class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
    
        while low < high:
            k = (low + high) // 2
            total_hrs = 0
            for bananas in piles:
                total_hrs += math.ceil(bananas/k)

            if total_hrs <= h:
                high = k

            else:
                low = k+1
        return low
