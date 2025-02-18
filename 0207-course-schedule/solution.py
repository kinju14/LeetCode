class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = {i: [] for i in range(numCourses)}
        visitedSet = set()

        for crs, pre_req in prerequisites:
            d[crs].append(pre_req)

        # print(d)
        def dfs(cr):
            if cr in visitedSet:
                return False
            
            if d[cr] == []:
                return True

            visitedSet.add(cr)
            for pre in d[cr]:
                if not dfs(pre):
                    return False
            visitedSet.remove(cr)
            d[cr] = []
            return True
                
        for crs in d:
            if not dfs(crs):
                return False
        return True


