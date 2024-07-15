# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = []
        d = {}

        for [parent, child, isLeft] in descriptions:
            children.append(child)
            
            temp_p = TreeNode(parent) if parent not in d else d[parent]
            temp_c = TreeNode(child) if child not in d else d[child]

            if isLeft:
                temp_p.left = temp_c
            else:
                temp_p.right = temp_c 

            d[parent] = temp_p
            d[child] = temp_c 
        
        for x in d.keys():
            if x not in children: return d[x]
 




            
