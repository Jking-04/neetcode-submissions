# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       length = 0

       curr = head
       while curr:
           curr=curr.next
           length +=1
       print(length)

       target = length - n

       dummy = ListNode(next=head)

       prev=dummy
       curr=head

       for i in range(target):
            prev=curr
            curr= curr.next

       prev.next=curr.next

       return dummy.next

           