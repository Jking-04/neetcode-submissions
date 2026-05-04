# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            adding = 0
            if l1:
                adding+=l1.val
            if l2:
                adding+=l2.val
            if carry:
                adding+=carry
                
            remainder = adding%10
            carry = adding//10
            
            curr.next = ListNode(val=remainder)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            curr = curr.next

        return dummy.next
