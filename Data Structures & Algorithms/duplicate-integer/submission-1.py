class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in range(len(nums)):
            if nums[num] in seen:
                return True
            seen.add(nums[num])
        return False

        