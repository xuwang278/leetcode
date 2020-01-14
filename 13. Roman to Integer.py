class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        ans = dic[s[0]]
        for i in range(1, len(s)):
            cur, pre = dic[s[i]], dic[s[i - 1]]
            if cur > pre:
                ans += cur - 2 * pre
            else:
                ans += cur
                
        return ans
        