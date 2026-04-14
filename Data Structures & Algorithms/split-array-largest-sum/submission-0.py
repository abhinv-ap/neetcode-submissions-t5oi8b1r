class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        h=sum(nums)
        res=0
        while l <= h:
            m=(l+h)//2
            curr=0
            c=1
            for i in nums:
                curr+=i
                if curr > m:
                    c+=1
                    curr = i
            if c > k:
                l=m+1
            else:
                res=m
                h=m-1
        return res

            



                




        