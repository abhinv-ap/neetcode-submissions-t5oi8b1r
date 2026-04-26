class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a=collections.Counter(tasks)
        heap=[]
        time=0
        queue=deque()
        for task , cnt in a.items():
            b=[-cnt,task]
            heap.append(b)
        
        heapq.heapify(heap)

        while heap or queue:
            time+=1
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(heap,queue[0][0])
                    queue.popleft()
            if heap:
                c=heapq.heappop(heap)
                c[0]+=1
                if c[0]:
                    queue.append([c,time+n+1])
        
        return time
            
            



        



    
        