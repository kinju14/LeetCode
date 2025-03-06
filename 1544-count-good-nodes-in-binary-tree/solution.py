# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_in_path):
            if not node:
                return

            if node.val >= max_in_path:
                self.count += 1
                max_in_path = node.val
            
            dfs(node.left, max_in_path)
            dfs(node.right, max_in_path)

            return
        dfs(root, root.val)
        return self.count
