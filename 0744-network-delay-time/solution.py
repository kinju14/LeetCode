class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weights = defaultdict(list)

        for [src, dest, time] in times:
            weights[src].append((dest, time))

        print(weights)
        result = 0
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited: 
                continue
            visited.add(n1)
            result = max(result, w1)

            for (n2, w2) in weights[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return result if len(visited) == n else -1
