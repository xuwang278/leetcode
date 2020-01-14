# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0: return r + 1
        if r == 0: return l + 1
        return min(l, r) + 1

    def minDepth(self, root: TreeNode) -> int:
        self.min = float("inf")
        if not root: return 0

        def dfs(root, height):
            if not root: return

            dfs(root.left, height + 1)
            dfs(root.right, height + 1)

            if not root.left and not root.right:
                self.min = min(self.min, height)
        
        dfs(root, 1)
        return self.min