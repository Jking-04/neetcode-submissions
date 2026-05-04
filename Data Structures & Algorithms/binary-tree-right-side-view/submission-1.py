# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        buffer = deque([root])
        in_curr_level = 1
        in_next_level=0

        right_seen_list = []

        while buffer:
            curr_node = buffer.popleft()
            in_curr_level -=1

            if curr_node:
                if curr_node.left:
                    buffer.append(curr_node.left)
                    in_next_level +=1
                if curr_node.right:
                    buffer.append(curr_node.right)
                    in_next_level +=1
            
                if in_curr_level == 0:
                    in_curr_level = in_next_level
                    in_next_level=0
                    right_seen_list.append(curr_node.val)
        
        return right_seen_list

        