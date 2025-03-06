# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxInLeft, minInRight):
            if not node:
                return True

            if node.val <= maxInLeft or node.val >= minInRight:
                return False
            
            return dfs(node.left, maxInLeft, node.val) and dfs(node.right, node.val, minInRight)

        return dfs(root, float('-inf'), float('inf'))
