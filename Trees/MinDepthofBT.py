#QUESTION:
#Given a binary tree, find minimum depth. 
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


#CODE:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if not root.right or not root.left:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
