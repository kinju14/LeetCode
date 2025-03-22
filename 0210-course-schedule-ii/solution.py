class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inDegree[crs] += 1

        q = deque([])
        for crs in range(numCourses):
            if not inDegree[crs]:
                q.append(crs)

        fin = 0
        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            fin += 1

            for c in graph[crs]:
                inDegree[c] -= 1
                if not inDegree[c]:
                    q.append(c)

        return res if fin == numCourses else []


