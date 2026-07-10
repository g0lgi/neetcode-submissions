class MinStack:

    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:        
        self.stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        minValue = 2**31
        for val in self.stack:
            if val < minValue:
                minValue = val
        return minValue
