# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root):
        buffer = deque([(root, float('-inf'), float('inf'))])

        while buffer:
            node, low, high = buffer.pop()

            if not node:
                continue

            if not (low < node.val < high):
                return False

            buffer.append((node.left, low, node.val))
            buffer.append((node.right, node.val, high))

        return True
