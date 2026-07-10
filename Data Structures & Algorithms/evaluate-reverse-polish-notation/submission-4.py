class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (len(token) > 1 and token[1:].isdigit):
                stack.append(int(token))
            else:
                if token == '+':
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    result = num_2 + num_1
                    stack.append(int(result))
                elif token == '-':
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    result = num_2 - num_1
                    stack.append(int(result))
                elif token == '*':
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    result = num_2 * num_1
                    stack.append(int(result))
                elif token == '/':
                    num_1 = stack.pop()
                    num_2 = stack.pop()
                    result = num_2 / num_1
                    stack.append(int(result))
            print(stack)
        return int(stack.pop())