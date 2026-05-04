# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def popper(node,target):
            if not node:
                return
            
            if node.right:
                node.right=popper(node.right,target)
            if node.left:
                node.left=popper(node.left,target)
            if not node.right and not node.left:
                if node.val == target:
                    return None 
            return node
        
        return popper(root,target)
        