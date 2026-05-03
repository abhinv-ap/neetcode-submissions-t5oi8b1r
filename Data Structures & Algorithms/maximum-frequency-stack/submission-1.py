class FreqStack:

    def __init__(self):
        self.arr=[[],[]]
        self.index=0
        self.counter={}        
        
    def push(self, val: int) -> None:
        self.counter[val]=1+self.counter.get(val,0)
        self.index=max(self.index,self.counter[val])
        if not self.arr[self.counter[val]]:
            self.arr.append([])
        self.arr[self.counter[val]].append(val)

    def pop(self) -> int:
        while not self.arr[self.index] and self.index >= 1:
            self.index-=1
        if self.index<1:
            return None
        a=self.arr[self.index].pop()
        self.counter[a]=self.counter.get(a,0)-1
        return a





        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()