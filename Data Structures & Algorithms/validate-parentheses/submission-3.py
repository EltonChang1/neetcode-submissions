class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for i in s:
            if i in brackets:
                if len(stack) == 0:
                    return False
                    
                elif brackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False