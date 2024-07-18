# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node: TreeNode, x: int, y: int):
            if not node: 
                return None

            if node.val == x or node.val == y:
                return node

            leftLCA = findLCA(node.left, x, y)
            rightLCA = findLCA(node.right, x, y)

            if leftLCA and rightLCA: return node

            if leftLCA: return leftLCA 
            else: return rightLCA
        
        z = findLCA(root, p.val, q.val)
        return z
        

