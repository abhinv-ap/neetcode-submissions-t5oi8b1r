class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i in a:
                return i
            else:
                a.append(i)
            
        
        return