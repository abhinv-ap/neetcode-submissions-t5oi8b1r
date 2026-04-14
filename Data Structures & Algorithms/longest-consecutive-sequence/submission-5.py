class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        m=1
        for i in nums:
            if i-1 not in nums:
                    c=1
                    while i+1 in nums :
                        c+=1
                        i=i+1
                    m=max(m,c)

        return m

        