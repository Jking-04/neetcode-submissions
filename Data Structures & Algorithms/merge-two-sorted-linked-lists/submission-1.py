# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = list1
        curr_l2 = list2

        dummy_head = ListNode()
        curr_new = dummy_head

        while curr_l1 and curr_l2:
            if curr_l1.val < curr_l2.val:
                curr_new.next = curr_l1
                curr_l1 = curr_l1.next
            else:
                curr_new.next = curr_l2
                curr_l2 = curr_l2.next

            curr_new = curr_new.next

        curr_new.next = curr_l1 or curr_l2

        return dummy_head.next


        
            
        