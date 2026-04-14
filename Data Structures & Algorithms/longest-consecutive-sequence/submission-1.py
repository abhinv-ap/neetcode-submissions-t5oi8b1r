class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxx=1
        count=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
            elif nums[i]-nums[i-1]==0:
                count=count
            else:
                maxx=max(maxx,count)
                count=1

        return max(maxx,count)
                


        