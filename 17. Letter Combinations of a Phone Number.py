class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or not len(digits):
            return []
        
        ans = []
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def dfs(i, cur):
            if i == len(digits):
                ans.append(cur)
                return
            
            s = d[ord(digits[i]) - ord('0')]
            for c in s:
                dfs(i + 1, cur + c)
                
        dfs(0, "")
        return ans
            
    def letterCombinations_iter(self, digits: str) -> List[str]:
        if not digits or not len(digits):
            return []

        ans = [""]
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for digit in digits:
            list = []
            for l in ans:
                s = d[ord(digit) - ord('0')]
                for c in s:
                    list.append(l + c)
            ans = list
        
        return ans