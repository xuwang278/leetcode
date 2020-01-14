# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        ans, q = [], [root]
        while q:
            size = len(q)
            list = []
            for _ in range(size):
                top = q.pop(0)
                list.append(top.val)
                if top.left: q.append(top.left)
                if top.right: q.append(top.right)
            ans.append(list)
        return ans[::-1] # make a copy of the same list in reverse order

    # Sol 2: dfs - version 1
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = [] # global 

        def dfs(root, level): # no need to pass in ans
            if not root: return []

            if level == len(self.ans):
                self.ans.append([])
            self.ans[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return self.ans[::-1]