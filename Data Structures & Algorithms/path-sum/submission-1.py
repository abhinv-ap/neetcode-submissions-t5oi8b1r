# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.tot=0
        target=targetSum
        def pathh(node,tot,target):
            if not node:
                return False
            tot+=node.val
            if not node.left and not node.right:
                if tot == target:
                    return True
                else:
                    return False
            
            
            return pathh(node.left,tot,target) or pathh(node.right,tot,target)
            
        
        return pathh(root,self.tot,target)
            


        