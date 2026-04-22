class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counter={'a':a,'b':b,'c':c}
        heap=[]
        for item,cnt in counter.items():
            if cnt:
                a=[-cnt,item]
                heap.append(a)
        
        heapq.heapify(heap)
        prev=None
        res=''
        while heap:
            a=heapq.heappop(heap)
            if prev:
                heapq.heappush(heap,prev)


                if -a[0]>1 and -prev[0]<-a[0]:
                    res += 2*a[1]
                    a[0]+=2
                else:
                    res+= a[1]
                    a[0]+=1
            else:

                if -a[0]>1:
                    res += 2*a[1]
                    a[0]+=2
                else:
                    res+= a[1]
                    a[0]+=1
            
            if a[0]:
                prev = [a[0],a[1]]
            else:
                prev=None
            
            if prev and not heap:
                return res
            
        return res



        