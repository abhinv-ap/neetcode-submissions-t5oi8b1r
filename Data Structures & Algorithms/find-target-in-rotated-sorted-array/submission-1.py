class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=int((l+r)/2)
            if(nums[mid]>nums[r]):
                l=mid+1
            else:
                r=mid

        if target <= nums[len(nums)-1]:
            l=l
            r=len(nums)-1
            while(l<=r):
                mid=int((l+r)/2)
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return mid
        else:
            r=l
            l=0
            while(l<=r):
                mid=int((l+r)/2)
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return mid

        return -1




        
        
        