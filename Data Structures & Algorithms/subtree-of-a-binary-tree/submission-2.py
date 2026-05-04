# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        return self.findRoot(root,subRoot)

    def findRoot(self,node,subRoot):
        if node and subRoot:
            if node.val == subRoot.val:
                if self.checkSubTree(node,subRoot):
                    return True
            
            if node.left and self.findRoot(node.left,subRoot):
                return True
            
            if node.right and self.findRoot(node.right,subRoot) :
                    return True

        return False


    def checkSubTree(self,node,subNode):
        if not node and not subNode:
            return True
        elif not node or not subNode:
            return False
        elif node.val != subNode.val:
            return False
                     
        else:
            return (
                self.checkSubTree(node.left,subNode.left) and 
                self.checkSubTree(node.right,subNode.right)
                )