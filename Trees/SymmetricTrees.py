#QUESTION:
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#CODE:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def mirrors(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            
            return (node1.val == node2.val) and mirrors(node1.left, node2.right) and mirrors(node1.right, node2.left)
        
        return mirrors(root, root)
