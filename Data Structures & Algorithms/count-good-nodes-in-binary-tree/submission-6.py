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
        self.res=0
        def check(node,maxx):
            if not node:
                return
            if node.val >= maxx:
                self.res += 1
            maxx=max(maxx,node.val)
            check(node.right,maxx)
            check(node.left,maxx)

        check(root,root.val)


        return self.res
            

        