# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        d = {}
        d[root.val] = [None, None]

        def parseTree(root: TreeNode):
            if root.left: 
                d[root.left.val] = [root.val, 'L']
                parseTree(root.left)

            if root.right: 
                d[root.right.val] = [root.val, 'R']
                parseTree(root.right)

        parseTree(root)

        if startValue == d[destValue][0]:
            return d[destValue][1]

        elif destValue == d[startValue][0]:
            return 'U'

        LCA = 0
        v1 = startValue
        v2 = destValue
        v1Parents, v2Parents = [startValue], [destValue]

        while v1:
            if d[v1][0]: v1Parents.append(d[v1][0])
            v1 = d[v1][0]

        while v2:
            if v2 in v1Parents:
                LCA = v2
                break
            v2 = d[v2][0]

        s1, s2 = '', ''
        v1 = startValue
        v2 = destValue

        while v1 != LCA:
            s1 += 'U'
            if d[v1][0]: v1 = d[v1][0]

        while v2 != LCA:
            s2 += d[v2][1]
            v2 = d[v2][0]

        return s1 + s2[::-1]

















        # LCA = 0      #if len(l) > 1 else l[0]
        # while d[l[0]][0]:
        #     num = l[0]
        #     if num in l[1:]: 
        #         LCA = num 
        #         break
        #     # if d[num][0]: 
        #     l.append(d[num][0])
        #     l.pop(0)
        # if LCA == 0:
        #     LCA = l[0]
        # print(LCA)

        # v1 = startValue
        # v2 = destValue

        # while v1 or v2:
        #     if v1 == v2:
        #         break
                
        #     print(v1, v2)

        #     if v1 != LCA and d[v1][0]:
        #         v1 = d[v1][0]
        #         s1 += 'U'
        #         if v1 == destValue:
        #             return s1

        #     if v2 != LCA and d[v2][0]:
        #         if d[v2][1]: 
        #             s2 += d[v2][1]
        #             print(s2)
        #         v2 = d[v2][0]
        #         print(f'v2: {v2}, dest: {destValue}')
        #         if v2 == startValue:
        #             return s2[::-1]
            
        # print(s1, s2)



        
