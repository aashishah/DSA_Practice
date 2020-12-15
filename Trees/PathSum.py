#QUESTION:
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        stack = [(root, sum)]
        while stack:
            node, curr_sum = stack.pop()
            if node:
                if not node.right and not node.left and node.val == curr_sum:
                    return True
                stack.append((node.right, curr_sum - node.val))
                stack.append((node.left, curr_sum - node.val))
        
        return False
