import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=1000000000
        res=r
        while(l<=r):
            t=0
            mid=int((l+r)/2)
            for i in piles:
                t=t+math.ceil(i/mid)
            if t<=h:
                res=mid
                r=mid-1
            elif t>h:
                l=mid+1
            
        return res




            

        

        