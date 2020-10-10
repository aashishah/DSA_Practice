#QUESTION: Find maximum depth of a binary tree. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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
        
        leftDepth = 1 + self.maxDepth(root.left)
        rightDepth = 1 + self.maxDepth(root.right)
        
        return max(leftDepth, rightDepth)

    #Explanantion:
    # maxDepth(3) = 2
        #   -> maxDepth(9) = 1
        #       -> maxDepth(None) = 0
        #       -> maxDepth(None) = 0
