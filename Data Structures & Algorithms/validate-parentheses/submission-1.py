class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_dict = {'{':'}','[':']','(':')'}
        stack = []

        for i in s:
            if i in paranthesis_dict:
                stack.append(i)
            elif stack and paranthesis_dict[stack[-1]] == i:
                stack.pop()
            else:
                return False
                
        return not stack
        