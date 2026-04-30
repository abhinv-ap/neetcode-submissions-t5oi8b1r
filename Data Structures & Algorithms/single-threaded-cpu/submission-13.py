class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ta=[]
        for i in range(len(tasks)):
            a=tasks[i]
            a.append(i)
            ta.append(a)
        
        ta.sort()
        time=ta[0][0]
        pntr=0
        heap=[]
        res=[]
        while pntr < len(ta) or heap:
            while pntr<len(ta) and time >= ta[pntr][0]:
                heapq.heappush(heap,ta[pntr][1:])
                pntr+=1
            if not heap:
                time+=ta[pntr][0]
                heapq.heappush(heap,ta[pntr][1:])
            a=heapq.heappop(heap)
            res.append(a[1])
            time+=a[0]

        return res[:len(ta)]

       