class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if(nums[i]==nums[i-1]) and i > 0:
                continue
            l,r=i+1,len(nums)-1
            target=nums[i]
            while(l<r):
                if (nums[l]+nums[r]==-(target)):
                    b=[nums[l],nums[r],target]
                    res.append(b)
                    r-=1
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                elif nums[l]+nums[r]>-(target):
                    r-=1
                else:
                    l+=1

        return res


                    

        
        