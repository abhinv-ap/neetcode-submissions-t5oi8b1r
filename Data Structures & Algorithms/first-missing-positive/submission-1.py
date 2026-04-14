class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxx=100000000
        if 1 not in nums:
            return 1
        for i in nums:
            if i >= 0:
                if i+1 not in nums:
                    maxx=min(maxx,(i+1))
        return maxx 


        