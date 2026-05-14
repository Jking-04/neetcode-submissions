# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")
        self.recursive_dfs(root)
        return self.max_path

    def recursive_dfs(self,node):
        best_left_branch = 0
        best_right_branch = 0 

        if node.left:
            best_left_branch =max(best_left_branch,self.recursive_dfs(node.left))
        if node.right:
            best_right_branch =max(best_right_branch,self.recursive_dfs(node.right))

        self.max_path = max(self.max_path,best_left_branch + node.val + best_right_branch)

        return max(best_left_branch +node.val,best_right_branch + node.val)
        
        


                

            
            
            
            


        

            
        