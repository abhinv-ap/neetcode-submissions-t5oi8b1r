# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.c=0
        def preorder(node,maxx):
            if not node:
                return
            if node.val>=maxx:
                maxx=max(maxx,node.val)
                self.c+=1
            preorder(node.left,maxx)
            preorder(node.right,maxx)
        preorder(root,root.val)
        return self.c
            
            
            

        