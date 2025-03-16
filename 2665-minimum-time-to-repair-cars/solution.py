class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepair(t):
            total = 0
            # (t / rank) ** 0.5 = cars
            for i in range(len(ranks)):
                total += int((t / ranks[i]) ** 0.5)
                if total >= cars:
                    return True
            return total >= cars

        l, r = 1, min(ranks) * cars * cars

        while l <= r:
            m = (l + r) // 2
            if canRepair(m):
                r = m-1
            else:
                l = m+1

        return l

        


