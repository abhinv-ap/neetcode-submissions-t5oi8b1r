class MinStack:

    def __init__(self):
        self.stak=[]
        self.minstak=[]
    
        

    def push(self, val: int) -> None:
        self.stak.append(val)
        if not self.minstak or val<=self.minstak[-1]:
            self.minstak.append(val) 
   
        

    def pop(self) -> None:
        if self.stak:
            if self.stak.pop()==self.minstak[-1]:
                self.minstak.pop()


        
    def top(self) -> int:
        if self.stak:
            return self.stak[-1]
        

    def getMin(self) -> int:
        if self.minstak:
            return self.minstak[-1]

        
