# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_n = None
        curr_n = head
        next_n = curr_n

        while next_n:
            next_n = curr_n.next
            curr_n.next = prev_n
            prev_n = curr_n
            curr_n = next_n

        return prev_n


    

        
            

       
        