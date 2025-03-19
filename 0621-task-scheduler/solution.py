class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = Counter(tasks)
        arr = [-count for count in hashMap.values()]
        heapq.heapify(arr)
        time = 0
        q = deque()

        while arr or q:
            time += 1

            if arr:
                count = heapq.heappop(arr)
                count += 1
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush(arr, q.popleft()[0])

        return time
        
