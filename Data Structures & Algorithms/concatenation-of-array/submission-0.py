class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        j = 0
        for i in range(len(nums)):
            ans.append(nums[j])
            j = j + 1

        return ans

        