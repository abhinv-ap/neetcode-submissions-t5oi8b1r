class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=None
        c2=None
        cc1=0
        cc2=0
        res=[]
        n=len(nums)
        for i in nums:
            if cc1==0 and i!=c2:
                c1=i
                cc1+=1
            elif cc2==0 and i!=c1:
                c2=i
                cc2+=1
            else:
                if i!=c1 and i!=c2:
                    cc1-=1
                    cc2-=1
                elif i==c1:
                    cc1+=1
                else:
                    cc2+=1
        k=0
        for i in nums:
            if i==c1:
                k+=1
        if k>n/3:
            res.append(c1)
        k=0
        for i in nums:
            if i==c2:
                k+=1
        if k>n/3:
            res.append(c2)
        
        return res
        
                





        