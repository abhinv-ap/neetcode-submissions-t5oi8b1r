class Solution:
    def reorganizeString(self, s: str) -> str:
        counter=collections.Counter(s)
        heap=[]
        for item,cnt in counter.items():
            a=[-cnt,item]
            heap.append(a)
        
        heapq.heapify(heap)
        res=''
        prev=None
        while heap:
            a=heapq.heappop(heap)
            if prev:
                heapq.heappush(heap,prev)
            a[0]+=1
            res+=a[1]
            if a[0]:
                prev = [a[0],a[1]]
            else:
                prev=None
            
            if prev and not heap:
                return ''
        
        return res 

            

        