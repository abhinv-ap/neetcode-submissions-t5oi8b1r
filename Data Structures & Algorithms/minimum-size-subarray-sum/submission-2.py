class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        maxl=float('inf')
        l=0
        agg=0
        for i in range(len(nums)):
            agg=agg+nums[i]
            while agg>=target:
                maxl= min(maxl,i-l+1)
                agg=agg-nums[l]
                l+=1    

        return maxl if maxl!=float('inf') else 0
    
        