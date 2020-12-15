#Same as Path sum but we print all possible paths with given sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        stack = [(root, [root.val], sum)]
        res = []
        while stack:
            node, path, curr_sum = stack.pop()
            if node:
                if not node.right and not node.left and node.val == curr_sum:
                    res.append(path)
                if node.right:
                    stack.append((node.right, path + [node.right.val], curr_sum - node.val))
                if node.left:
                    stack.append((node.left, path + [node.left.val], curr_sum - node.val))
        
        return res

    #Variation: Count the no. of paths present:
    def countPaths(root, sum_):
        if root is None:
            return []
        stack = [(root, sum)]
        count = 0
        while stack:
            node, curr_sum = stack.pop()
            if node:
                if not node.right and not node.left and node.val == curr_sum:
                    count += 1
                if node.right:
                    stack.append((node.right, curr_sum - node.val))
                if node.left:
                    stack.append((node.left, curr_sum - node.val))
        
        return count
    
    
