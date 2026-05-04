# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        in_curr_level = 1
        in_next_level = 0

        nested_list = []
        curr_level_list = []

        buffer = deque([root])
        
        while buffer:
            curr_node = buffer.popleft()
            in_curr_level -= 1

            if curr_node:
                curr_level_list.append(curr_node.val)

                if curr_node.left:
                    buffer.append(curr_node.left)
                    in_next_level +=1
                if curr_node.right:
                    buffer.append(curr_node.right)
                    in_next_level +=1
            
            if in_curr_level == 0:
                in_curr_level = in_next_level
                in_next_level = 0

                if curr_level_list:
                    nested_list.append(curr_level_list.copy())
                    curr_level_list.clear()

        return nested_list




        