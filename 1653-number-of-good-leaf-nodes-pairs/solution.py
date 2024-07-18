# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leavesPath = []

        def parseTree(node: TreeNode, s: string):
            if node.left:
                parseTree(node.left, s + 'l')
            if node.right: 
                parseTree(node.right, s + 'r')
            if not node.left and not node.right:
                leavesPath.append(s)

        parseTree(root, '')
        res = 0

        n = len(leavesPath)
        for i in range(n-1):
            for j in range(i+1, n):
                p1, p2 = leavesPath[i], leavesPath[j]
                x = 0
                while x < len(p1) and x < len(p2) and p1[x] == p2[x]:
                    x += 1 

                if ((len(p1) - x) + (len(p2) - x)) <= distance:
                    res += 1
        return res
