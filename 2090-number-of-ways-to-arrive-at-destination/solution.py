class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))


        minHeap = [(0, 0)]
        ways = [0] * n
        shortestPath = [float('inf')] * n
        shortestPath[0] = 0
        ways[0] = 1

        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if dist > shortestPath[node]:
                continue
            
            for nei, w in graph[node]:
                newDist = dist + w

                if newDist < shortestPath[nei]:
                    shortestPath[nei] = newDist
                    ways[nei] = ways[node]
                    heapq.heappush(minHeap, (newDist, nei))

                elif newDist == shortestPath[nei]:
                    ways[nei] += ways[node]
                
        return ways[n-1] % (10**9 + 7)
