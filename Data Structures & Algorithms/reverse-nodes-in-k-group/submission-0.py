# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        f1=dummy     
        while f1.next:
            prev=None
            f2=f1.next
            check=f2
            c=0
            while check and c<k+1:
                check=check.next
                c+=1
            if c<k:
                break
            
            f3=f2
            for i in range(k):
                temp=f2.next
                f2.next=prev
                prev=f2
                f2=temp
            
            f1.next = prev
            f3.next=f2

            f1=f3

        return dummy.next


            


            


            
        