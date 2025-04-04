# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return None, depth
            
            lnode, ldepth = dfs(node.left, depth+1)
            rnode, rdepth = dfs(node.right, depth+1)

            if ldepth > rdepth:
                return lnode, ldepth
            elif rdepth > ldepth:
                return rnode, rdepth
            return node, ldepth

        node, _ = dfs(root, 0)
        return node
