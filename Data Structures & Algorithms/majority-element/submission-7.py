class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ##try the boyer moore voting algorithm
        majelem=nums[0]
        freq=0
        for i in nums:
            if i == majelem:
                freq+=1
            else:
                freq-=1
            
            if freq<0:
                majelem=i
        
        return majelem
             
        