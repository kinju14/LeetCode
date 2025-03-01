# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: TreeNode, curr_res: int):
            nonlocal res
            if node is None:
                return

            curr_res += 1

            res = max(res, curr_res)
            dfs(node.left, curr_res)
            dfs(node.right, curr_res)


        dfs(root, 0)
        return res


