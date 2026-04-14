# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def pre(node):
            if not node:
                return
            pre(node.left)
            pre(node.right)
            a.append(node.val)

        
        pre(root)
        return a

        
        