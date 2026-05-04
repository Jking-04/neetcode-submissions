# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameNode(p,q)

    def isSameNode(self,p_node,q_node):
        if p_node == None and q_node==None:
            return True
        elif p_node == None or q_node==None:
            return False
        elif p_node.val != q_node.val:
            return False
        else:
        
            left_subtree_same = self.isSameNode(p_node.left,q_node.left)
            right_subtree_same = self.isSameNode(p_node.right,q_node.right)
        
            return left_subtree_same and right_subtree_same
        