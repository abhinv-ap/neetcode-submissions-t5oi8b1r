# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1=[]
        t2=[]

        def inorder(node,t1):
            if not node:
                t1.append(None)
                return
            t1.append(node.val)
            inorder(node.right,t1)
            inorder(node.left,t1)

        inorder(p,t1)
        inorder(q,t2)

        return t1==t2
            
        