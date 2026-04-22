class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heap=stones
        heapq.heapify(heap)

        while len(heap)>1:
            a=heapq.heappop(heap) * (-1)
            b=heapq.heappop(heap) * (-1)
            res=abs(a-b)
            if res:
                heapq.heappush(heap,(-1)*res)
        
        return -heap[0] if heap else 0
        