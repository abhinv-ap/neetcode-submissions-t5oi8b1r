class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        res=len(nums)
        l=0
        summ=0
        for i in range(len(nums)):
            summ=summ+nums[i]
            while summ>= target:
                res=min(res,i-l+1)
                summ-=nums[l]
                l=l+1
            

        return res
            


        