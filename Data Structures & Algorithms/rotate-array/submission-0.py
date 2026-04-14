class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        temp = nums[:len(nums) - k]   # first n-k elements
        nums[:k] = nums[-k:]          # last k elements to front
        nums[k:] = temp               # rest goes after
