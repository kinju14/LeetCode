class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))
            if x != y:
                heapq.heappush(stones, -(x-y))

        return abs(stones[0]) if stones else 0
