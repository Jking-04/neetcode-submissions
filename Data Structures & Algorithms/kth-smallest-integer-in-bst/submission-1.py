# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        buffer = deque()
        node = root
        element = 0 

        while buffer or node:
        # 1. Go as far left as possible
            while node:
                buffer.append(node)
                node = node.left

            # 2. Backtrack (this is the "coming back up")
            node = buffer.pop()

            element +=1
            if element == k:
                return node.val

            # 3. Go right
            node = node.right

            
            
        