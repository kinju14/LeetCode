# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [root]
        result = []

        while queue:
            qLen = len(queue)
            temp = []
            while qLen>0:
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left: 
                    queue.append(curr.left) 
                if curr.right:
                    queue.append(curr.right) 
                qLen -= 1
            result.append(temp)
        return result








        
