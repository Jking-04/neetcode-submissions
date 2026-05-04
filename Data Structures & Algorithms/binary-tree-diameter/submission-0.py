# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _,max_diam = self.MaxDiameterOfNode(root)
        return max_diam
        
    def MaxDiameterOfNode(self,root):
        if root.left:
            left_max_depth,left_diameter = self.MaxDiameterOfNode(root.left)
        else:
            left_max_depth = 0
            left_diameter = 0

        if root.right:
            right_max_depth,right_diameter = self.MaxDiameterOfNode(root.right)
        else:
            right_max_depth = 0
            right_diameter = 0

        max_diameter = max(left_diameter,right_diameter,left_max_depth + right_max_depth) 

        return max(left_max_depth,right_max_depth)+1,max_diameter