# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        buffer = deque([(root.val,root)])
        good_nodes = 0
        while buffer:
            max_val,curr_node = buffer.pop()
        
            if curr_node:
                if curr_node.val>=max_val:
                    print(curr_node.val)
                    good_nodes+=1

                max_val = max(max_val,curr_node.val)
                if curr_node.left:
                    buffer.append((max_val,curr_node.left))
                if curr_node.right:
                    buffer.append((max_val,curr_node.right))
        return good_nodes

                
        