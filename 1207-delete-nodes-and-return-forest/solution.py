# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = [root]

        def parseTree(tree: TreeNode):
            if tree.val in to_delete:
                roots.remove(tree)
                if tree.left and tree.left.val not in to_delete: roots.append(tree.left)
                if tree.right and tree.right.val not in to_delete: roots.append(tree.right)

            if tree.left: 
                if tree.left.val in to_delete:
                    if tree.left.left: 
                        roots.append(tree.left.left)
                        parseTree(tree.left.left)
                    if tree.left.right: 
                        roots.append(tree.left.right)
                        parseTree(tree.left.right)
                    tree.left = None
                else:
                    parseTree(tree.left)

            if tree.right: 
                if tree.right.val in to_delete:
                    if tree.right.left: 
                        roots.append(tree.right.left)
                        parseTree(tree.right.left)
                    if tree.right.right: 
                        roots.append(tree.right.right)
                        parseTree(tree.right.right)
                    tree.right = None
                else:
                    parseTree(tree.right)

        parseTree(root)
        return roots
