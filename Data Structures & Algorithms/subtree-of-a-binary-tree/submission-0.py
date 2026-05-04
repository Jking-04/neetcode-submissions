# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findRoot(root,subRoot)

    def findRoot(self,node,subRoot):
        found_here=False
        found_l=False
        found_r=False

        if node.val == subRoot.val:
            found_here=self.checkSubTree(node,subRoot)
        
        if node.left:
            found_l=self.findRoot(node.left,subRoot)
        
        if node.right:
            found_r=self.findRoot(node.right,subRoot)

        return found_here or found_l or found_r

    def checkSubTree(self,node,subNode):
        if not node and not subNode:
            return True
        elif not node or not subNode:
            return False
        elif node.val == subNode.val:
            return self.checkSubTree(node.left,subNode.left) and self.checkSubTree(node.right,subNode.right)          
        else:
            return False