# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_bal,_ = self.is_balanced_node(root)
        return is_bal

    def is_balanced_node(self,curr_node):
        is_balance= True

        if curr_node == None:
            return True,0

        left_is_bal,left_depth = self.is_balanced_node(curr_node.left)
        right_is_bal,right_depth = self.is_balanced_node(curr_node.right)

        print(curr_node.val)
        print(left_depth)
        print(right_depth)
        print("_______")
        is_balance = (left_is_bal and right_is_bal) and abs(left_depth-right_depth)<=1

        return is_balance,max(left_depth,right_depth)+1

        
        