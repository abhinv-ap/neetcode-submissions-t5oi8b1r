# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=list1
        curr2=list2
        head=ListNode()
        dummy=head
        while curr and curr2:
            if curr.val>curr2.val:
                head.next=curr2
                head=head.next
                curr2=curr2.next
            else:
                head.next=curr
                head=head.next
                curr=curr.next
            
        if curr:
            head.next=curr
        if curr2:
            head.next=curr2
        
        return dummy.next

            
            



        