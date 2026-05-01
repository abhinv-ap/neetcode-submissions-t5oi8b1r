class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        filled=0
        heap=[]
        seq=[]
        for cap,start,end in trips:
            seq.append([start,end,cap]) 
        seq.sort()

        for i in seq:
            heapq.heappush(heap,i[1:])
            curr=i[0]
            while heap and heap[0][0] <= curr:
                a=heapq.heappop(heap)
                filled-=a[1]
            
            filled+=i[2]
            if filled > capacity:
                return False
            
        return True




        