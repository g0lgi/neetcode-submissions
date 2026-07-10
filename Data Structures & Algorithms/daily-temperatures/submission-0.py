class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0] * (len(temperatures))
        for i in range(len(temperatures)):
            counter = 0
            if len(stack) > 0:
                while (len(stack) > 0) and temperatures[i] > temperatures[stack[-1]]:
                    counter = i - stack[-1]
                    result[stack[-1]] = counter
                    stack.pop()
            stack.append(i)
            # print(i)
            # print(stack)
            # print(result)
        return result