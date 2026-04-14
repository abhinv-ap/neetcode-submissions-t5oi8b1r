# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.res=True
        def bal(node):
            if not node:
                return 0
            r=bal(node.right)
            l=bal(node.left)
            height=abs(l-r)
            if height > 1:
                self.res=False
            return 1+max(l,r)
        bal(root)
        return self.res
        