class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        num, a = 0, x
        while a != 0:
            num = num * 10 + a % 10
            a = a // 10
        
        return num == x