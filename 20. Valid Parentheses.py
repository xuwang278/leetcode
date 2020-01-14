class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(' : ')', '[' : ']', '{' : '}'}
        for c in s:
            if c in dic:
                stack.append(c)
            elif len(stack) == 0 or dic[stack.pop()] != c:
                return False
        return len(stack) == 0


    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    l = stack.pop()
                    if l == '(' and c != ')': 
                        return False
                    if l == '[' and c != ']':
                        return False
                    if l == '{' and c != '}':
                        return False
        
        return len(stack) == 0