class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.final=[]
        def subs(i,res,nums,final):
            if i >= len(nums):
                final.append(res.copy())
                return
            val=nums[i]
            res.append(val)
            subs(i+1,res,nums,final)
            res.pop()
            subs(i+1,res,nums,final)

        subs(0,res,nums,self.final)

        return self.final