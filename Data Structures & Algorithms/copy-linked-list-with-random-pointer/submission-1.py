"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        oldtonew={}
        curr = head
        while curr:
            oldtonew[curr]=Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                oldtonew[curr].next=oldtonew[curr.next]
            else:
                oldtonew[curr].next=None
            if curr.random:
                oldtonew[curr].random=oldtonew[curr.random]
            else:
                oldtonew[curr].random=None
            curr=curr.next

        return oldtonew[head]


        

        