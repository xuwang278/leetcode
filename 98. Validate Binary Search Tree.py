# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Sol 1:
    # Time: O(n) - n: # of nodes in tree
    # Space: O(h) - h: height of tree
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        
        def dfs(root):
            if not root:
                return True
            if not dfs(root.left):
                return False
            
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val >= root.val:
                    return False
                self.pre = root
            
            return dfs(root.right)

        return dfs(root)

    # this version is wrong
    def isValidBST(self, root: TreeNode) -> bool:
        pre = None # cann't set local variable as None

        def dfs(root):
            if not root:
                return True
            if not dfs(root.left):
                return False
            
            if not pre:
                pre = root
            else:
                if self.pre.val >= root.val:
                    return False
                pre = root
            
            return dfs(root.right)

        return dfs(root)

    # this version is wrong
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None # set instance attribute here is problemetic because it'll reset in every following recursive calls

        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        
        if not self.pre:
            self.pre = root
        else:
            if self.pre.val >= root.val:
                return False
            self.pre = root
        
        return self.isValidBST(root.right)

    # this version works
    def __init__(self):
        self.pre = None # set instance attribute in constructor out of isValidBST
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            print(1)
            return True
        
        if not self.isValidBST(root.left):
            print(2)
            return False
        
        if not self.pre:
            self.pre = root
        else:
            if self.pre.val >= root.val:
                print(3)
                return False
            self.pre = root
            
        return self.isValidBST(root.right)

    # Sol 2:
    # Time: O(n)
    # Space: O(h)
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(root, min, max):
            if not root:
                return True
            if root.val >= max or root.val <= min:
                return False
            return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)

        return dfs(root, float('-inf'), float('inf'))

    # Sol 3:
    # Time: O(n) 
    # Space: O(n)
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []
        def dfs(root):
            if not root: 
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root) # build inorder seqpeuce
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True
