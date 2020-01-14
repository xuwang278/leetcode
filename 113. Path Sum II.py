# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root: return ans
        self.dfs(root, sum, [], ans)
        return ans
    
    def dfs(self, root, sum, list, ans):
        if not root: return
        
        list.append(root.val) 
        
        # successful case is one layer higher than leaf
        if sum == root.val and not root.left and not root.right:
            ans.append([] + list)
            list.pop()
            return
        
        self.dfs(root.left, sum - root.val, list, ans)
        self.dfs(root.right, sum - root.val, list, ans)
        list.pop()
        