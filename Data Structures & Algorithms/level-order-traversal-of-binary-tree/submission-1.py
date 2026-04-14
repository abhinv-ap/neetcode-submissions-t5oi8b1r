# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue=deque()
        queue.append(root)

        while queue:
            temp=[]
            for i in range(len(queue)):
                if queue[0].left:
                    queue.append(queue[0].left)
    
                if queue[0].right:
                    queue.append(queue[0].right)
                
                temp.append(queue.popleft().val)
            
            res.append(temp)

        return res

        


        