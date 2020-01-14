# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Sol 1: bfs
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        q = [(root.left, root.right)]
        while q:
            l, r = q.pop(0)
            if not l and not r: continue
            if not l or not r: return False
            if l.val != r.val: return False
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True

     # Sol 2: dfs
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        def dfs(l, r):
            if not l and not r: return True
            if not l or not r: return False
            if l.val != r.val: return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        
        return dfs(root.left, root.right)