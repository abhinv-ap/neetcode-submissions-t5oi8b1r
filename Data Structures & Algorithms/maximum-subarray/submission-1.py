class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        r=0
        summ=0
        res=max(nums)
        for i in range(len(nums)):
            summ=summ+nums[i]
            res=max(res,summ) 
            if summ<0:
                summ=0
                        
                        
        return res
            
            