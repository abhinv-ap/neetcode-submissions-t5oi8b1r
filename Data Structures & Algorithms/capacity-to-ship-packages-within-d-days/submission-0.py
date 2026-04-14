class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while(l<=r):
            wt=0
            t=1
            mid=int((l+r)/2)
            for i in weights:
                wt=wt+i
                if(wt>mid):
                    t=t+1
                    wt=i
            if t<=days:
                res=mid
                r=mid-1
            else:
                l=mid+1

        return res


