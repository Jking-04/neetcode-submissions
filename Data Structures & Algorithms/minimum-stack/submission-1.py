class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minimum=val
        else:
            minimum = min(val,self.getMin())

        self.stack.append((val,minimum))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        temp = self.stack[-1]
        return temp[0]

    def getMin(self) -> int:
        temp = self.stack[-1]
        return temp[1]

        
