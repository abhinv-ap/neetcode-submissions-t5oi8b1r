# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxx=0
        def dia(node):
            if not node.right and not node.left:
                return 1
            diam = ((dia(node.left) if node.left else 0) + (dia(node.right) if node.right else 0))
            self.maxx=max(self.maxx, diam)
            return 1+max(dia(node.left) if node.left else 0 , dia(node.right) if node.right else 0)
            
        dia(root)
        return self.maxx






        