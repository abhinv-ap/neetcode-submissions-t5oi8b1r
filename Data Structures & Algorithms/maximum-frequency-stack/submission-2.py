class FreqStack:

    def __init__(self):
        self.heap=[]
        self.cntr={}
        self.counter=0

    def push(self, val: int) -> None:
        self.counter+=1
        self.cntr[val]=1+self.cntr.get(val,0)
        elem=[-self.cntr[val],-self.counter,val]
        heapq.heappush(self.heap,elem)

    def pop(self) -> int:
        if not self.heap:
            return None   
        a=heapq.heappop(self.heap)
        self.cntr[a[2]]=self.cntr.get(a[2],0)-1
        return a[2]
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()