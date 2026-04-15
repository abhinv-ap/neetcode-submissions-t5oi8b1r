class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        res=h

        while l<=h:
            cap=(l+h)//2
            load=0
            t=1
            for i in weights:
                if load+i>cap:
                    t+=1
                    load=i
                else:
                    load+=i
            if t>days:
                l=cap+1
            else:
                h=cap-1
                res = cap
        
        return res
            
            






        