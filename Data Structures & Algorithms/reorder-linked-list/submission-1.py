# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = head
        slow = head

        prev = None

        while fast and fast.next:
            prev=slow
            slow= slow.next
            fast= fast.next.next
            
        prev.next = None

        curr = slow
        
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev= curr
            curr = next_node
            

        l1 = head
        l2 = prev
        dummy = ListNode()
        curr = dummy

        flip_flag = True

        while l1 or l2:
            if flip_flag and l1:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next 
            flip_flag = not flip_flag

            curr = curr.next

        while dummy:
            print(dummy.val)
            dummy = dummy.next

        
        
