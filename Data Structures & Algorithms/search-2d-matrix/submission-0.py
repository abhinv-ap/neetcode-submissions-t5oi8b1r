class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        c=None
        for i in range(len(matrix)):
            if target>=matrix[i][0] and target<=matrix[i][-1]:
                c=i


    
        if c == None:
            return False
        
        l=0
        r=len(matrix[c])-1
        while(l<=r):
            m=int((r+l)/2)
            if matrix[c][m]==target:
                return True
            elif matrix[c][m]>target:
                r=m-1
            else:
                l=m+1
        return False

        