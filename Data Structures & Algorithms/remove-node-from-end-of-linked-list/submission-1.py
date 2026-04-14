# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        dummy = ListNode(0, head)        
        c=0
        while(p):
            c+=1
            p=p.next
        p=dummy
        for i in range(c-n):
            p=p.next

        p.next=p.next.next
        return dummy.next



        