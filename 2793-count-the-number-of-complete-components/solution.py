class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def bfs(node):
            q = deque([node])
            comp = []
            edge = 0
            
            while q:
                curr = q.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                comp.append(curr)
                for nei in graph[curr]:
                    q.append(nei)
                    edge += 1

            return comp, edge//2

        res = 0
        for node in range(n):
            if node not in visited:
                compNodes, compEdges = bfs(node)
                k = len(compNodes)
                if compEdges == k * (k-1) // 2:
                    res += 1

        return res


