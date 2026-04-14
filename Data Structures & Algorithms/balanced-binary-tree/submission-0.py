# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.c=1
        def bal(node):
            if not node:
                return 0
            l=bal(node.left)
            r=bal(node.right)
            if abs(l-r)>1:
                self.c=0
            return max(l,r)+1
        
        bal(root)
        
        if self.c==1:
            return True
        else:
            return False
        



        