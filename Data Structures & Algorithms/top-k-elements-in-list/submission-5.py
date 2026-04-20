class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=collections.Counter(nums)
        res=[[]for _ in range(len(nums) + 1)]
        out=[]
        for i,j in a.items():
            res[j].append(i)
        res=res[::-1]
        print (res)
        l=len(nums)
        for i in res:
            if len(out) == k:
                break
            
            for x in i:
                if len(out)<k:
                    out.append(x)
        return out


  
        