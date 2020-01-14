class Solution:
    def reverse(self, x: int) -> int:         
        sign = 1 if x > 0 else -1
        ans, x = 0, abs(x)
        while x != 0:
            ans = ans * 10 + x % 10
            print(ans)
            if ans > 2**31 - 1 or ans  < (-2)**31:
                return 0
            x = x // 10
        return sign * ans
        
# >>> x = -123
# >>> x % 10
# 7