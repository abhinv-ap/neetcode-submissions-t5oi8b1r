# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        if not root:
            return 0
        def depth(node):
            if not node:
                return 0
            return 1+max(depth(node.right),depth(node.left))

        def dob(node):
            if not node:
                return
            
            self.ans=max(self.ans,depth(node.right)+depth(node.left))

            dob(node.right)
            dob(node.left)
        
        dob(root)

        return self.ans

        
            

        