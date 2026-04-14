# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        a = root
        while a.val != key:
            temp=a
            if a.val>key:
                a=a.left
            else:
                a=a.right
            if not a:
                return root
        
        if not a.right and not a.left:
            if a==root:
                return None
            if temp.right and temp.right.val == key:   
                temp.right=None
            else:
                temp.left=None

        elif not a.right or not a.left:
            child=a.right if a.right else a.left
            if a==root:
                return child
            
            if temp.right.val == key:
                temp.right=a.right if a.right else a.left
            else:
                temp.left=a.right if a.right else a.left

        else:
            temp=a
            a=a.right
            while a.left != None:
                a=a.left
            
            temp.val=a.val
            temp.right=self.deleteNode(temp.right,temp.val)
        return root



        
            

        


        