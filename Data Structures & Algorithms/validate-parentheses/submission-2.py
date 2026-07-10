class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False