class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.pop_from1 = False

    def push(self, x: int) -> None:
        if not self.stack1 and not self.stack2:
            self.stack1.append(x)
            self.pop_from1 = True

        if self.pop_from1:
            self.stack2.append(x)
        else:
            self.stack1.append(x)

    def pop(self) -> int:
        if self.pop_from1 and not self.stack1:
            while self.stack2:
                x = self.stack2.pop()
                self.stack1.append(x)
            self.pop_from1 = True                
            return self.stack1.pop()
        elif not self.pop_from1 and not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
            self.pop_from1 = False        
            return self.stack2.pop()

        if self.pop_from1:
           return  self.stack1.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        if self.pop_from1 and self.stack1:
            return self.stack1[-1]
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        

# 1 . [ 1 - 2 - 3]

# 2. []
