# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hashSet = set()
        self.root = self.recover(root)

    def find(self, target: int) -> bool:
        if target in self.hashSet:
            return True
        return False

    def recover(self, root: Optional[TreeNode]):
        root.val = 0
        self.hashSet.add(root.val)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                node.left.val = 2 * node.val + 1
                self.hashSet.add(node.left.val)
                queue.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.hashSet.add(node.right.val)
                queue.append(node.right)

        return root


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
