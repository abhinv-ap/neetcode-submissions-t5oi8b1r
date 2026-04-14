# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        for i in range (left-1):
            curr=curr.next
        a=curr
        b=curr.next
        c=b
        prev=None
        for i in range (right-left+1):
            temp=c.next
            c.next=prev
            prev=c
            c=temp
        
        a.next=prev
        b.next=c

        return dummy.next




        