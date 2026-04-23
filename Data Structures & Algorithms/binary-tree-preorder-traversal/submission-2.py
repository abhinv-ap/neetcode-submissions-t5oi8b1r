# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        self.res=[]

        def preord(node):
            if not node:
                return
            
            self.res.append(node.val)
            preord(node.left)
            preord(node.right)

        preord(root)

        return self.res
        