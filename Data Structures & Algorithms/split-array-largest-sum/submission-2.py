class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minn=max(nums)
        maxx=sum(nums)
        res=maxx

        while minn <= maxx:

            mid=(minn+maxx)//2

            splits=1
            summ=0
            for i in nums:
                summ+=i
                if summ > mid:
                    summ=i
                    splits+=1
            
            if splits > k:
                minn=mid+1
            else:
                maxx=mid-1
                res=min(res,mid)
        
        return res

            
        