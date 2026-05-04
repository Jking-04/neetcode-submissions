# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.reverseNode(root)
        return root


    def reverseNode(self,node):
        node.left,node.right = node.right,node.left

        if node.left:
            self.reverseNode(node.left)
        
        if node.right:
            self.reverseNode(node.right)
        