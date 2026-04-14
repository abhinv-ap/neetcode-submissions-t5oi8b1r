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
            return None
    

        curr=head

        while curr:
            temp=curr.next
            node=Node(curr.val,curr.next)
            curr.next=node
            curr=temp

        curr=head

        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr=curr.next.next

        curr=head
        ans=head.next

        while curr:
            temp=curr.next
            curr.next=curr.next.next if curr.next else None
            curr=temp
        return ans

        


        

        