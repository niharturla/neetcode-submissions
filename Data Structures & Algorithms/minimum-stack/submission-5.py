class MinStack:
    [1,2,4]
    def __init__(self): # intialize stack object
        self.stack = [] # [val, min_element at that point in time]

    def push(self, val: int) -> None:
        # find curr min val
        if not self.stack:
            curr_min = val
        else:
            curr_min = min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
         if self.stack:
            return self.stack[-1][1]

    
