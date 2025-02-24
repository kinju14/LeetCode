class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)

        for [x, y] in edges:
            graph[y].append(x)
            graph[x].append(y)

        print(f"Initial graph: {graph}")

        bobTime = [-1] * len(amount)

        def dfs(bobNode: int, curr: set, time: int):
            bobTime[bobNode] = time
            if bobNode == 0:
                return True

            for n in graph[bobNode]:
                if n != curr and dfs(n, bobNode, time+1):
                    return True
            
            bobTime[bobNode] = -1
            return False

        dfs(bob, -1, 0)
        
        maxProfit = float('-inf')

        def aliceDFS(node: int, currProfit: int, time: int, curr: int):
            nonlocal maxProfit
            if bobTime[node] == -1 or time < bobTime[node]:
                currProfit += amount[node]
            elif time == bobTime[node]:
                currProfit += amount[node]//2

            isLeaf = True
            for n in graph[node]:
                if n != curr:
                    isLeaf = False
                    aliceDFS(n, currProfit, time+1, node)
                
            if isLeaf:
                maxProfit = max(maxProfit, currProfit)
            
        aliceDFS(0, 0, 0, -1)
        return maxProfit




