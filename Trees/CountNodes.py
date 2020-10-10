#QUESTION:
#Count the number of nodes in a binary tree.

#CODE:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + self.maxDepth(root.right) + self.maxDepth(root.left)
