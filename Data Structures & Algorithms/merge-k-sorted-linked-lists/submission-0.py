# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(first_node.val,i,first_node) for i,first_node in enumerate(lists)]
        heapq.heapify(heap)

        dummy_root = ListNode()
        curr = dummy_root

        done = 0
        total = len(lists)
        unique_id = len(lists)-1

        while done < total:
            best_min = heapq.heappop(heap)
            curr.next = best_min[2]

            new_node = best_min[2].next
            
            if new_node:
                unique_id += 1
                heapq.heappush(heap,(new_node.val,unique_id,new_node))
            else:
                done += 1
            
            curr = curr.next

        return dummy_root.next    

                     