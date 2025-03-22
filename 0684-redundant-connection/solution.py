class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]

                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

                return True
            else:
                return False

        for u, v in edges:
            if not union(u, v):
                return [u, v]

