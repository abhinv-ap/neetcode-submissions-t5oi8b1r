# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invertt(root):
            if not root:
                return 
            root.right,root.left=root.left,root.right
            invertt(root.right)
            invertt(root.left)
        invertt(root)
        return root
        