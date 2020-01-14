# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Sol 1: dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1

    # Sol 2: bfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        depth = 0
        q = [root]
        while q:
            size = len(q)
            for _ in range(size):
                top = q.pop(0)
                if top.left: 
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            depth += 1
            
        return depth