class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(set(nums))
        if a == len(nums):
            return False
        else:
            return True
        