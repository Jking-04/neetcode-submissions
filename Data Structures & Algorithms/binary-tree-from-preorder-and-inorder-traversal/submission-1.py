# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        in_order_idx = {}
        for i,node_val in enumerate(inorder):
            in_order_idx[node_val] = i

        for new_node_val in preorder:
            new_node = TreeNode(val = new_node_val)

            if not root:
                root = new_node
            
            else:
                node = root
                while True:
                    if in_order_idx[new_node_val] < in_order_idx[node.val]:
                        if node.left:
                            node = node.left
                        else:
                            node.left = new_node
                            break
                    else:
                        if node.right:
                            node = node.right
                        else:
                            node.right = new_node
                            break
        return root
       



            
        
        