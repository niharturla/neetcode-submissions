# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # [1,2,3,5] state of stack at leaf 5 
        # store the max after each pop
        # for each node in the stack after the pop, check for its left child
        # then pop node to move up a level
        # then move to right child 
        # keep doing this until current node is null or stack is empty, meaning there are no more nodes to traverse

        max_d = 0

        def dfs(root):
            if root is None:
                return 0
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            diameter = left_h+right_h
            nonlocal max_d
            max_d = max(max_d,diameter)

            return 1+max(left_h,right_h)
        dfs(root)
        return max_d

