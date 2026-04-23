class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        a=collections.Counter(nums)
        heap=[]
        for item,cnt in a.items():
            b=[-cnt,item]
            heap.append(b)
        
        heapq.heapify(heap)

        res=[]

        for i in range(k):
            if heap:
                a=(heapq.heappop(heap))
                res.append(a[1])
            
        return res[::-1]

        
        