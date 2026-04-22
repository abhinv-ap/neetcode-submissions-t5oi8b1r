class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res=[]
        heap=[]
        for i in range(len(points)):
            distance=math.sqrt((points[i][0])**2+(points[i][1])**2)
            p=[distance,i]
            heap.append(p)

        heapq.heapify(heap)

        for i in range(k):
            if heap:
                a=heapq.heappop(heap)
                res.append(points[a[1]])
        
        return res


        