class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        inDegree = defaultdict(int)

        for r, ingList in zip(recipes, ingredients):
            inDegree[r] = len(ingList)
            for ing in ingList:
                graph[ing].append(r)
        
        q = deque(supplies)
        res = []
        while q:
            item = q.popleft()
            if item in inDegree:
                res.append(item)
            
            for r in graph[item]:
                inDegree[r] -= 1
                if inDegree[r] == 0:
                    q.append(r)
        
        return res

