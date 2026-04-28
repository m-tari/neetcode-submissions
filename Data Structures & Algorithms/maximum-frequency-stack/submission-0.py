from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)  # element -> freq
        self.stacks = defaultdict(list)  # freq -> [elements]
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.count[val]        
        self.stacks[freq+1].append(val)
        self.count[val] += 1
        self.max_freq = max(self.max_freq, freq + 1)

    def pop(self) -> int:
        element = self.stacks[self.max_freq].pop()
        self.count[element] -= 1
        
        if self.count[element] == 0:
            del self.count[element]

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
            
        return element

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()