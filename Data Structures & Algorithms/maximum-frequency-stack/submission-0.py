class FreqStack:

    def __init__(self):
        self.s=[]
    
    def push(self, val: int) -> None:
        freq = 0
        for layer in self.s:
            if val in layer:
                freq += 1 
        if freq == len(self.s):
            self.s.append([val])
        else:
            self.s[freq].append(val)
    def pop(self) -> int:
        val = self.s[-1].pop()
        if not self.s[-1]:
            self.s.pop()    
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()