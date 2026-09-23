# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs on every node
        if not root:
            return 0
        stack = [(root, float('-inf'))]
        good = 0

        while stack:
            node, maxValue = stack.pop()
            if node.val >= maxValue:
                good += 1
            curr_max = max(maxValue, node.val)
            if node.left:
                stack.append((node.left, curr_max))

            if node.right:
                stack.append((node.right, curr_max))
               
        return good




