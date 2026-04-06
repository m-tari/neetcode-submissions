class MyQueue:

    def __init__(self):
        self.s_in = []  # Stack that stores all push opertation
        self.s_out = []  # Stack that receive all pop operations

    def _move(self):
        if not self.s_out:
            while self.s_in:
                x = self.s_in.pop()
                self.s_out.append(x)

    def push(self, x: int) -> None:
        self.s_in.append(x)

    def pop(self) -> int:
        self._move()
        return self.s_out.pop()

    def peek(self) -> int:
        self._move()
        return self.s_out[-1] # same behavior as standard deque: raises IndexError on empty

    def empty(self) -> bool:
        return False if self.s_in or self.s_out else True
        

# 1 . [ 1 - 2 - 3]

# 2. []
