# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a=root
        if not a:
            root=TreeNode(val)
            return root
        while(True):
            if val < a.val:
                if a.left==None:
                    a.left=TreeNode(val)
                    break
                else:
                    a=a.left

            if val > a.val:
                if a.right==None:
                    a.right=TreeNode(val)
                    break
                else:
                    a=a.right
        return root




        