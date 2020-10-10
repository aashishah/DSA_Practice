#QUESTION:
#Given a binary tree, determine if it is a valid binary search tree (BST).
#Assume a BST is defined as follows:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.


#Note: Can be done with inorder traversal. Traversed tree is in sorted order if valid bst, else not.



#CODE:
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        stack = []
        inorder = float('-inf')
        count = 0
        while stack or root:
            count += 1
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= inorder:
                return False
            
            inorder = root.val
            root = root.right
        
        return True
