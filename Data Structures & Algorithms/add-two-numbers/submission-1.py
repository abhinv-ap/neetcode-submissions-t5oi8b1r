# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rum=ListNode()
        curr=rum
        c=0
        while(l1 and l2):
            a=l1.val+l2.val+c
            if(a>9):
                c=1
                a=a%10
            else:
                c=0
            temp=ListNode(a)
            curr.next=temp
            curr=curr.next
            l1=l1.next
            l2=l2.next

        while(l1):
            a=l1.val+c
            if(a>9):
                c=1
                a=a%10
            else:
                c=0
            temp=ListNode(a)
            curr.next=temp
            curr=curr.next
            l1=l1.next
            
        while(l2):
            a=l2.val+c
            if(a>9):
                c=1
                a=a%10
            else:
                c=0
            temp=ListNode(a)
            curr.next=temp
            curr=curr.next
            l2=l2.next

        if (c==1):
            temp=ListNode(c)
            curr.next=temp
            
            
        return rum.next


        