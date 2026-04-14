# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def yovalid(node,left,right):
            if not node:
                return True
            if left<node.val<right:
                return yovalid(node.right,node.val,right) and yovalid(node.left,left,node.val)
            else:
                return False

        return yovalid(root,float("-inf"),float("inf"))



        
        