# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        def invert(node):
            if not node.right and not node.left:
                return
            
            temp = node.right
            temp2= node.left

            node.right= temp2
            node.left= temp
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
        invert (root)
        return root
            


        