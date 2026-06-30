class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {'(':')','[':']','{':'}'}
        stack = []
        for i in s:
            if i in parentheses_dict:
                stack.append(i)
            else:
                if stack and parentheses_dict[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack
        