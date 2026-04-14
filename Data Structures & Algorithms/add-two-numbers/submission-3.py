# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=l1,l2
        c=0
        summ=0
        dummy=ListNode()
        curr=dummy
        while curr1 and curr2:
            summ = curr1.val+curr2.val + c
            if summ>9:
                summ=summ%10
                c=1
            else:
                c=0
            curr1=curr1.next
            curr2=curr2.next
            a=ListNode(summ)
            curr.next=a
            curr=curr.next

        while curr1:
            summ = curr1.val + c
            if summ>9:
                summ=summ%10
                c=1
            else:
                c=0
            curr1=curr1.next
            a=ListNode(summ)
            curr.next=a
            curr=curr.next
        
        while curr2:
            summ = curr2.val + c
            if summ>9:
                summ=summ%10
                c=1
            else:
                c=0
            curr2=curr2.next
            a=ListNode(summ)
            curr.next=a
            curr=curr.next
        

        if c==1:
            a=ListNode(1)
            curr.next=a
            curr=curr.next


        return dummy.next
            







        