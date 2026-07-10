class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in {'[', '{', '('}:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
                if s[i] == ')' and top != '(':
                    return False
                stack.pop()
        return len(stack) == 0