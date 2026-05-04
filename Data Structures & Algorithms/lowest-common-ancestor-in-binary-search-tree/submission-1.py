# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        value = node.val

        max_search = max(p.val,q.val)
        min_search = min(p.val,q.val)

        while node:
            if min_search<=node.val and node.val<=max_search:
                return node
            elif min_search<=node.val and max_search<=node.val:
                node = node.left
            elif node.val<=min_search and node.val<=max_search:
                node = node.right
        


        