class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        v1=None
        c2=0
        v2=None
        for i in nums:
            if i == v1:
                c1+=1
            elif i == v2:
                c2+=1
            
            elif c1==0:
                v1=i
                c1+=1
            
            elif c2==0:
                v2=i
                c2=1
            else:
                c1-=1
                c2-=1
        
        res = []
        for c in [v1, v2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)

        return res
            

        