"""
QUESTION:
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

"""

#CODE:
def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        alt = True
        res = []
        depth = 1
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                        queue.append(node.left)
                if node.right:
                        queue.append(node.right)
            
            avg = sum(level) / len(level)
            res.append(avg)
            
        return res
