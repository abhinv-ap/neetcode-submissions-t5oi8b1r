class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        heap=[]
        for item,cnt in dic.items():
            a=[-cnt,item]
            heap.append(a)
        
        heapq.heapify(heap)

        a=heapq.heappop(heap)

        return a[1]
        