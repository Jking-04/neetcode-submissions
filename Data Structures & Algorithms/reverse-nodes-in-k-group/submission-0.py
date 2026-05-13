# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        stopper = dummy

        done = False

        while stopper:
            curr_n = stopper    
            for _ in range(k):
                if stopper.next:
                    stopper = stopper.next
                else:
                    done = True
            
            if done == True:
                break

            temp_1 = curr_n
            temp_2 = stopper.next

            reverse_tail = curr_n.next
            next_n = curr_n.next
            
            while curr_n != stopper:
                prev=curr_n
                curr_n = next_n
                next_n = next_n.next

                curr_n.next = prev
            
            temp_1.next = curr_n
            reverse_tail.next = temp_2

            stopper = reverse_tail
            
            print("___")
        return dummy.next
        