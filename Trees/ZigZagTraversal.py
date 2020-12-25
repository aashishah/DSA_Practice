"""
QUESTION:
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

#CODE:
def zigzagTraversal(root):
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
            
            if depth % 2 == 0:
                level = level[::-1]
            depth += 1
            res.append(level)
            
        return res
