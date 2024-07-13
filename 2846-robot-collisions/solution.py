
class Solution:
    def survivedRobotsHealths(self, positions: List[int], health: List[int], directions: str) -> List[int]:
        n = len(positions)
        l = []
        d = {}
        for i in range(n):
            l.append([positions[i], directions[i], health[i]])
            d[positions[i]] = health[i]

        l = sorted(l, key= lambda x: x[0])
        
        res = []
        stack = list(list())
        for i in range(n):
            if len(stack) == 0 or l[i][1] != 'L':
                stack.append(l[i])
            while len(stack) != 0 and l[i][1] != stack[-1][1]:
                if stack[-1][2] == l[i][2]:
                    temp = stack.pop()
                    if temp[0] in d: del d[temp[0]] 
                    if l[i][0] in d: del d[l[i][0]] 
                    break
                elif stack[-1][2] > l[i][2]:
                    stack[-1][2] -= 1
                    d[stack[-1][0]] -= 1
                    if l[i][0] in d: del d[l[i][0]]
                    break
                else:
                    temp = stack.pop()
                    if temp[0] in d: del d[temp[0]]
                    l[i][2] -= 1
                    d[l[i][0]] = l[i][2]

        for k,v in d.items():
            res.append(v)

        return res
