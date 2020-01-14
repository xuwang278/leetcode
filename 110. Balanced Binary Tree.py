# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            return 1 + max(l, r)

        l = height(root.left)
        r = height(root.right)
        if abs(l - r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # Sol 2: early stop
    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True

        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1:
                self.balanced = False
            return 1 + max(l, r)
            
        height(root)
        return self.balanced