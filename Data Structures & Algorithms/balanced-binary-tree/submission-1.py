# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use dfs
        # once we get to the lead, check for left height and right height
        # if abs(left-right) > 1 -> return false
        
        max_h = 0
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right=dfs(root.right)
            nonlocal max_h
            max_h = max(max_h, abs(left-right))
            return 1+max(left,right)
        dfs(root)
        return max_h <= 1
        




            
