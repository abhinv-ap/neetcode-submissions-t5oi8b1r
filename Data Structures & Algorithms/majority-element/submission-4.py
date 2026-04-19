class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        val=0
        for i in nums:
            if count == 0:
                val = i
            
            if val != i:
                count-=1
            
            else:
                count+=1
        
        return val
            

        