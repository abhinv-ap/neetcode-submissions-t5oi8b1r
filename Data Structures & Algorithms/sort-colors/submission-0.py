class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors={0:0,1:0,2:0}
        for i in nums:
            colors[i]=colors.get(i,0)+1
        nums[:] = [0]*colors[0] + [1]*colors[1] + [2]*colors[2]