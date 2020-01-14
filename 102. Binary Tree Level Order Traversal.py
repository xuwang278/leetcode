# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Sol 1: bfs - version 1
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return ans

    # Sol 1: bfs - version 2
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            next = []
            for node in level:
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)
            level = next
        return ans

    # Sol 1: bfs - version 3
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level]) # load nodes in level to ans
            level = [child for node in level for child in (node.left, node.right) if child] # update level to be non-null child(ren) of each node in level
        return ans

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
        return self.ans

    # Sol 2: dfs - version 2
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = [] # local

        def dfs(root, level, ans): # pass in local ans
            if not root: return []

            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)

            dfs(root.left, level + 1, ans)
            dfs(root.right, level + 1, ans)

        dfs(root, 0, ans)
        return ans
