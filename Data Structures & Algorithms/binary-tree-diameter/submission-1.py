# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def motu(root):
            if not root :
                return 0
            l=motu(root.left)
            r=motu(root.right)
            self.res=max(self.res,l+r)
            return max(l,r)+1
        motu(root)
        return self.res
        


        

            


        