class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)
        
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else 0
        