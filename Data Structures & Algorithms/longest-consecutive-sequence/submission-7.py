class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        l=0
        res=0
        for i in nums:
            l=0
            if i-1 not in nums:
                while i+l in nums:
                    l+=1
            
            res=max(res,l)
        
        return res

         

        