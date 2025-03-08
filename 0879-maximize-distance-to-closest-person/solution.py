class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0 if seats[0] else -1
        res = 0

        for i in range(1, len(seats)):
            if seats[i]:
                if l == -1:
                    res = i
                else:
                    res = max(res, (i-l)//2)
                l = i
        res = max(res, len(seats)-1-l)
        
        return res



