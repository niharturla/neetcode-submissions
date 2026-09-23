# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        res = deque()

        # get in-order traversal

        def inorder(root):
            nonlocal k
            stack = []
            node = root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node=node.right

        return inorder(root)

            


