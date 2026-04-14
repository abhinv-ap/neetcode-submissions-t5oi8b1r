# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dep(node):
            if not node.right and not node.left:
                return 1     
            return 1+max(dep(node.right) if node.right else 0,dep(node.left) if node.left else 0)

        return dep(root)
        