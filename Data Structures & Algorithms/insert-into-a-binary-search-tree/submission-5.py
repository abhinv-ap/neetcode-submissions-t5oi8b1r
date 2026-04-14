# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        node=TreeNode(val)
        if not root:
            return node
        def ins(root,node):
            if root.val>node.val:
                if not root.left:
                    root.left=node
                    return
                ins(root.left,node)
            else:
                if not root.right:
                    root.right=node
                    return
                ins(root.right,node)

        ins(root,node)
        return root