class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        minn=max(nums)
        maxx=sum(nums)
        res=maxx
        while minn <= maxx:
            curr=0
            counter=1
            mid=(minn+maxx)//2
            for i in nums:
                curr+=i
                if curr > mid:
                    counter+=1
                    curr=i
                
            if counter>k:
                minn=mid+1
            else:
                maxx=mid-1
                res=min(mid,res)
        
        return res

        


        