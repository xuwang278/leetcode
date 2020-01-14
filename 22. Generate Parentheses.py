class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        ans = []
        self.dfs(n, n, '', ans)
        return ans

    def dfs(self, l, r, s, ans):
        if l < 0 or r < 0 or l > r:
            return
        
        if l == 0 and r == 0:
            ans.append(s)
            return

        self.dfs(l - 1, r, s + '(', ans)
        self.dfs(l, r - 1, s + ')', ans)

