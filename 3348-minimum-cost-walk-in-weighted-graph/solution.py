class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        r1, r2 = self.find(x), self.find(y)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
                self.rank[r2] += self.rank[r1]
            else:
                self.parent[r2] = r1
                self.rank[r1] += self.rank[r2]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        cost = {}

        for u, v, w in edges:
            r = uf.find(u)
            if r not in cost:
                cost[r] = w
            else:
                cost[r] &= w

        res = []
        for u, v in query:
            r1, r2 = uf.find(u), uf.find(v)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(cost[r1])

        return res
